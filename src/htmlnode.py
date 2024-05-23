class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("yet")

    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join(f'{k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf requires value")
        if self.tag is None:
            return self.value
        props_line = ""
        if self.props is not None and len(self.props) > 0:
            props_line = f" {self.props_to_html()}"

        return f"<{self.tag}{props_line}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent has to have tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent has to have children")

        inner = "".join(f"{child.to_html()}" for child in self.children)

        props_line = ""
        if self.props is not None and len(self.props) > 0:
            props_line = f" {self.props_to_html()}"
        return f"<{self.tag}{props_line}>{inner}</{self.tag}>"
