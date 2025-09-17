class SVGElement:
    def __init__(self, type_, attributes=None, inner_text=None, children=None, id_=None):
        self.type = type_
        self.attributes = attributes or {}
        self.inner_text = inner_text
        self.children = children or []
        self.id = id_ or self.attributes.get("id")

    def to_svg_string(self):
        attr_str = " ".join(f'{k}="{v}"' for k, v in self.attributes.items())
        if self.inner_text or self.children:
            children_str = "".join(child.to_svg_string() for child in self.children)
            return f'<{self.type} {attr_str}>{self.inner_text or ""}{children_str}</{self.type}>'
        else:
            return f'<{self.type} {attr_str} />'

    def clone(self):
        return SVGElement(
            type_=self.type,
            attributes=self.attributes.copy(),
            inner_text=self.inner_text,
            children=[c.clone() for c in self.children]
        )
import uuid
import xml.etree.ElementTree as ET
from collections import OrderedDict

def normalize_value(val):
    try:
        return float(val) if '.' in val else int(val)
    except:
        return val

def parse_style_string(style):
    result = {}
    for part in style.split(";"):
        if ":" in part:
            key, val = part.strip().split(":")
            result[key.strip()] = val.strip()
    return result

class SVGElement:
    def __init__(self, type_, attributes=None, inner_text=None, children=None, id_=None):
        self.type = type_
        self.attributes = attributes or {}
        self.inner_text = inner_text
        self.children = children or []
        self.id = id_ or self.attributes.get("id")

    def to_svg_string(self):
        attr_str = " ".join(f'{k}="{v}"' for k, v in self.attributes.items())
        if self.inner_text or self.children:
            children_str = "".join(child.to_svg_string() for child in self.children)
            return f'<{self.type} {attr_str}>{self.inner_text or ""}{children_str}</{self.type}>'
        else:
            return f'<{self.type} {attr_str} />'

    def clone(self):
        return SVGElement(
            type_=self.type,
            attributes=self.attributes.copy(),
            inner_text=self.inner_text,
            children=[c.clone() for c in self.children]
        )


class SVGDocument:
    def __init__(self, elements=None, root_attributes=None):
        self.elements = elements or []
        self.root_attributes = root_attributes or {}

    @classmethod
    def from_svg(cls, svg_string):
        root = ET.fromstring(svg_string)
        elements = cls._parse_elements(root)
        return cls(elements, root.attrib)

    @staticmethod
    def _parse_elements(xml_element):
        elements = []
        for child in xml_element:
            tag = child.tag.split("}")[-1]
            el = SVGElement(
                type_=tag,
                attributes=child.attrib,
                inner_text=child.text,
                children=SVGDocument._parse_elements(child)
            )
            elements.append(el)
        return elements

    def to_svg_string(self):
        body = "\n  ".join(el.to_svg_string() for el in self.elements)
        return f'<svg xmlns="http://www.w3.org/2000/svg">\n  {body}\n</svg>'

    from collections import OrderedDict

    def to_pastelvg(self):
        pastel = OrderedDict()
        pastel["pastelvg"] = "0.1"
        pastel["id"] = f"doc-{uuid.uuid4().hex[:4]}"
        pastel["name"] = "Untitled"

        if "width" in self.root_attributes:
            pastel["width"] = normalize_value(self.root_attributes["width"])
        if "height" in self.root_attributes:
            pastel["height"] = normalize_value(self.root_attributes["height"])

        pastel["content"] = [self._element_to_pvg(el) for el in self.elements]
        return pastel

    def _element_to_pvg(self, el):
        out = OrderedDict()
        out["type"] = el.type
        out["id"] = el.id or f"{el.type}-{uuid.uuid4().hex[:4]}"

        known_keys = ["x", "y", "cx", "cy", "r", "width", "height", "fill", "font-size", "text-anchor"]

        for k in known_keys:
            if k in el.attributes:
                out[k] = normalize_value(el.attributes[k])

        if "stroke" in el.attributes:
            out["stroke"] = {"color": el.attributes["stroke"]}
        if "stroke-width" in el.attributes:
            if "stroke" not in out:
                out["stroke"] = {}
            out["stroke"]["width"] = normalize_value(el.attributes["stroke-width"])

        if "transform" in el.attributes:
            out["transform"] = self._parse_transform(el.attributes["transform"])

        # Children
        if el.type == "g":
            out["type"] = "group"
            out["children"] = [self._element_to_pvg(c) for c in el.children]

        # Text content
        if el.type == "text" and el.inner_text:
            out["content"] = [{"text": el.inner_text.strip()}]

        return out

    def _parse_transform(self, value):
        # Currently only supports translate(x y)
        if value.startswith("translate"):
            parts = value.strip("translate()").replace(",", " ").split()
            tx = normalize_value(parts[0])
            ty = normalize_value(parts[1]) if len(parts) > 1 else 0
            return ["translate", tx, ty]
        return None
