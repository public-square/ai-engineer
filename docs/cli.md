# Command Line Interface
`ai-engineer` is a simple command line interface covering the existing API
targets and offering some administrative capabilites.

## RAG Repository Management
Repository contents are vectorized in a Pinecone index to support RAG.
Keeping the Pinecone index up to date is necessary to get current results
from RAG-enabled prompts.

### Vectorize a Github Repository
Repositories are added to the index as discrete namespaces, specified as
`{owner}/{repository}/{branch}`. No output is produced if the operation
succeeds.

```bash
./ai-engineer ragindex vectorize \
--repo 'public-square/ai-engineer/main'
```

### List Indexed Repositories
Currently indexed reporitories are listed as an array of strings. The strings
are in the same format used to index them.

Note that after an index operation completes, there may be a brief delay before
the new repository is available for listing.

```bash
./ai-engineer ragindex list
```

```
['public-square/ai-engineer/main']
```

### Delete a Repository from the Index
```bash
./ai-engineer ragindex delete \
--repo 'public-square/ai-engineer/main'
```

### LLM Chat
Prompts may be sent to the LLM without context, if desired.

```bash
./ai-engineer chat \
--prompt 'Make me laugh in 50 words or less.'
```

To provide retrieval augmented generation based on a specific repository,
specify that repository with a `--repo` argument.

```bash
./ai-engineer chat \
--repo 'public-square/ai-engineer/main' \
--prompt "What is the curl command I should use to hit the ping API target?"
```

## Local Clone Management
The Pinecone index is used only for RAG. Reading and writing files is done
locally with a clone of the repository.

Repository strings for cloning match those used for index management, and
are specified with  `--repo` argument.

Local clones should be viewed as transient. Be sure to commit any important
changes and push them upstream regularly.

Note that clones are stored in the directory specified in the environment
variable and can be used the same way any other github clone is used.

### Making a Local Repository Clone
Note that creating a clone is destructive. If that clone currently exists,
it will be overwritten and any changes that have not been pushed upstream will
be lost.

```bash
./ai-engineer clone create --repo public-square/ai-engineer/main
```

### Deleting a Local Repository Clone
The delete command removes a local repository clone entirely. Any changes that
have not been pushed upstream will be lost.

```bash
./ai-engineer clone delete --repo public-square/ai-engineer/main
```

### Listing Local Clones

```bash
./ai-engineer clone list
```

## Administrative Functions

### Create Pinecone Index
For a fresh install where the index does not exist, use the CLI to create
a new index as defined in environment variables. The value of `dimension` used
to create the index must match the encoding model to successfully index
repositories for RAG.

```bash
./ai-engineer setup newindex
```

```
{'name': 'ai-engineer', 'dimension': '1536', 'metric': 'cosine'}
```

### Ping
To ensure that the code executes, use `ping` to send a string and observe that
it is returned reverses.
```bash
./ai-engineer-cli.py ping --text '123 456'
```

```
{ 'ping': '123 456', 'pong': '654 321' }
```
