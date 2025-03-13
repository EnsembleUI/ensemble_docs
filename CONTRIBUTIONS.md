# Ensemble Documentation

This repo contains Ensemble docs hosted at [docs.ensembleui.com](https://docs.ensembleui.com).

## Contributing to the docs directly on GitHub

Because Ensemble docs are created directly from the markdown in this repo, you can use the GitHub web editor to edit and propose changes to the docs directly from your browser without any knowledge of git. To do that, find the markdown file with the docs you want to edit and follow [GitHub's instructions](https://docs.github.com/en/free-pro-team@latest/github/managing-files-in-a-repository/editing-files-in-another-users-repository) to edit and propose changes to a markdown file. Once approved, the docs will be updated immediately.

## Local Development

This documentation was created from [Nextra](https://nextra.site).

First, run `pnpm i` to install the dependencies.

Then, run `pnpm dev` to start the development server and visit localhost:3000.

To use a different port, run `pnpm next dev -p <port_number>`.

## Deployment & hosting

This site is hosted on Vercel, and updated automatically when the main branch is updated.
