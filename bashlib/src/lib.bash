# HERE-INCLUDE ./src/util.bash
# HERE-INCLUDE ./src/dumpjson.bash
# HERE-INCLUDE ./src/usage.bash
# HERE-INCLUDE ./src/parse_argv.bash

if ! which "ocrd" >/dev/null 2>/dev/null;then
    ocrd__raise "ocrd not in \$PATH"
fi

if ! declare -p "OCRD_TOOL_JSON" >/dev/null 2>/dev/null;then
    ocrd__raise "Must set \$OCRD_TOOL_JSON"
elif [[ ! -r "$OCRD_TOOL_JSON" ]];then
    ocrd__raise "Cannot read \$OCRD_TOOL_JSON: $OCRD_TOOL_JSON"
fi

if ! declare -p "argv" >/dev/null 2>/dev/null ;then
    ocrd__raise "Must set \$argv"
fi

