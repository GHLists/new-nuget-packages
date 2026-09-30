# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-09-30 09:22 UTC

New packages created between 2026-09-30 08:20 UTC and 2026-09-30 09:22 UTC.

[Full CSV](data/new-nuget-packages-2026-09-30T09-22-20-735873Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-30 08:37:07 | [MorseCode.StagedConstruction](https://www.nuget.org/packages/MorseCode.StagedConstruction) | 0.1.0 | MorseCode Software LLC | Construction of immutable objects in ordered stages, with no access to a partly… |
| 2026-09-30 08:43:17 | [MimeMagic](https://www.nuget.org/packages/MimeMagic) | 4.0.0 | red,si618 | .NET wrapper for libmagic, bundling native libmagic binaries for Windows, Linux… |
| 2026-09-30 08:48:20 | [MorseCode.Mvvm](https://www.nuget.org/packages/MorseCode.Mvvm) | 0.1.0 | MorseCode Software LLC | Building blocks for view models written in a functional reactive style on SodaF… |
| 2026-09-30 08:49:12 | [SQLSentinel.Mcp](https://www.nuget.org/packages/SQLSentinel.Mcp) | 2.3.1 | Takudzwa Mawarire | SQL Sentinel MCP Server - Advanced SQL Server monitoring and diagnostics for AI… |
| 2026-09-30 08:53:09 | [Fusi.Docx.Encoding](https://www.nuget.org/packages/Fusi.Docx.Encoding) | 1.0.5 | Daniele Fusi | DOCX encoding conversion components. |
| 2026-09-30 08:58:16 | [Toamaisutaa.OpenApi](https://www.nuget.org/packages/Toamaisutaa.OpenApi) | 0.8.0 | Pianonic | OpenAPI security schemes for Toamaisutaa: a bearer scheme for locally issued to… |
| 2026-09-30 08:58:18 | [Toamaisutaa.PasswordHashing.Argon2](https://www.nuget.org/packages/Toamaisutaa.PasswordHashing.Argon2) | 0.8.0 | Pianonic | Opt-in Argon2id password hashing for Toamaisutaa. Nothing else references this… |
| 2026-09-30 08:58:19 | [Toamaisutaa.PasswordValidation.Hibp](https://www.nuget.org/packages/Toamaisutaa.PasswordValidation.Hibp) | 0.8.0 | Pianonic | Opt-in Have I Been Pwned breach check for Toamaisutaa password validation. Wrap… |
| 2026-09-30 08:58:20 | [Toamaisutaa.Passkeys](https://www.nuget.org/packages/Toamaisutaa.Passkeys) | 0.8.0 | Pianonic | Opt-in passkey (WebAuthn) authentication for Toamaisutaa: registration and asse… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
