# langgraph_mistral
This uses the mistral function call to bind to route for graph state called by supervisor.
According to langchain, the official open ai function call is needed for the routing carried out by the node to edge of new state machine used by the orchestration architecture of langgraph. but support for local llm engine like mistral is not available until now , this repo contain a experimental function that mimic open ai and allow langgraph to be used locally on your local llm server.
