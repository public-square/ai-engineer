# API Endpoints
The system can run as a django API, exposing functionality to http requests.

The sample `curl` commands below expose functionality and responses for
programmatic execution. It is assumed that the `jq` system command is installed
to format `JSON` output.

## Ping
The ping target responds with proof of life. It responds with `pong` containing
the reverse of `ping`.

```bash
curl --silent -X POST -H "Content-Type: application/json" \
http://localhost:8001/api/ping/ \
-d '{"ping": "123 456 789"}' | jq
```

## RAG Repository Management
To faciliate intelligent responses, github repositories are vectorized for
retrieval augmented generation.

Github repositories may be specified as `owner/repo/branch`. Branch is optional,
and a leading `/` is ignored if present. If the branch is not specified, `main`
is assumed.

### Vectorize a Repository for RAG
To make a repository available for RAG, each is added to the index in a discrete
namespace. That namespace is referenced when making RAG-enabled LLM requests.

```bash
curl -X POST -H "Content-Type: application/json" \
http://localhost:8001/api/ragindex/vectorize/ \
-d '{"repository": "/public-square/ai-engineer/main"}' | jq
```

### List RAG Repositories
The current list of repositories indexed for RAG is available for verification.

```bash
curl --silent -X GET -H "Content-Type: application/json" \
http://localhost:8001/api/ragindex/list/ | jq
```

### Delete a Repository RAG Namespace
Remove a repository entirely from the index.

```bash
curl --silent -X DELETE -H "Content-Type: application/json" \
http://localhost:8001/api/ragindex/delete/ \
-d '{"repository": "public-square/ai-engineer/main"}' | jq
```

## LLM Prompts
Prompts may be executed against the LLM with a specified repository for RAG:

```bash
curl --silent -X POST -H "Content-Type: application/json" \
http://localhost:8001/api/chat/prompt/ -d @- << EOF |
{
  "prompt": "What is the curl command I should use to hit the ping API target?",
  "repository": "public-square/ai-engineer/main"
}
EOF
jq
```

Simple LLM prompts may also be executed:

```bash
curl --silent -X POST -H "Content-Type: application/json" \
http://localhost:8001/api/chat/prompt/ -d @- << EOF |
{
  "prompt": "Make me laugh in 50 words or less."
}
EOF
jq
```


