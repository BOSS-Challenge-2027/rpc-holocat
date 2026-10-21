RPC Holocat: Code Challenge
===========================


The goal of this code challenge is to add a new RPC method to Bitcoin Core: `holocat`

To accomplish this you will need to build Bitcoin Core from source, add your code
changes, test your code changes, commit and push.

> [!TIP]
> Do not push to any other branch besides `main`

This repository already contains the Bitcoin Core source code at the `v32.0` tag.
One extra functional test has been added which asserts that the new command follows
the specification. Don't break any of the existing functional tests either!

When you push your work to the `main` branch, a GitHub workflow will build your
code and run the test. The action will give you a Pass ✅ or Fail ❌ report.

> [!IMPORTANT]
> This is the ONLY code challenge in the BOSS 2027 program that will give you
> explicit, binary feedback! Don't get used to it!

## RPC `holocat` specification

### Usage:

`bitcoin-cli holocat`
(no parameters)

### Expected result:

- Output MUST represent, in some way, something about the current blockchain state
- Output MUST change when a new block is added to the chain, because the current blockchain state has been changed
- Output MUST always return the same value for the same chain state

The actual content of the output result is totally up to you. Be creative!
Impress us! Think of something unusual, funny, interesting. It doesn't
have to be particularly useful but that would be nice too! 🐱