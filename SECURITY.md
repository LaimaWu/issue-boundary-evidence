# Security

Issue Boundary Evidence treats GitHub issue titles, bodies, comments, code blocks, and linked text as untrusted input.

The tool is intentionally read-only:

- it never executes code, shell commands, or scripts found in issues or comments;
- GitHub API access is limited to `GET` requests;
- non-GitHub URLs may be recorded as evidence, but are not fetched;
- linked repositories are not cloned or executed.

If you discover a security issue in this tool, please use GitHub's private security reporting feature when available. Avoid posting exploit details in a public issue before a private report has been acknowledged.
