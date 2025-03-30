
## Communication
respond valid json with fields
thoughts: array thoughts before execution in natural language
tool_name: use tool name
tool_args: key value pairs tool arguments

no other text

### Response example
~~~json
{
    "thoughts": [
        "instructions?",
        "solution steps?",
        "processing?",
        "actions?"
    ],
    "tool_name": "name_of_tool",
    "tool_args": {
        "arg1": "val1",
        "arg2": "val2"
    }
}
~~~