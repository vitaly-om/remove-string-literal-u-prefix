import libcst


class UPrefixTransformer(libcst.CSTTransformer):
    def leave_SimpleString(
        self, original_node, updated_node,
    ):
        if original_node.value.startswith('u"') or original_node.value.startswith("u'"):
            return updated_node.with_changes(value=original_node.value[1:])
        return updated_node


def remove_u_prefix(code: str) -> str:
    cst = libcst.parse_module(code)
    result = cst.visit(UPrefixTransformer())
    return result.code
