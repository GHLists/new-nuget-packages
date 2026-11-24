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

## Latest list — 2026-11-24 04:20 UTC

New packages created between 2026-11-24 03:18 UTC and 2026-11-24 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-24T04-20-58-204121Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-24 03:49:43 | [Nefarius.Tools.DDG](https://www.nuget.org/packages/Nefarius.Tools.DDG) | 1.0.0 | Benjamin Höglinger-Stelzer | Grow a mounted Windows Dev Drive's VHDX, GPT partition, and ReFS filesystem in… |
| 2026-11-24 04:05:39 | [AIKernel.Providers.DocumentSearch](https://www.nuget.org/packages/AIKernel.Providers.DocumentSearch) | 0.1.4 | Takuya Sogawa | Read-only local keyword search for Markdown and text, with reproducible documen… |
| 2026-11-24 04:06:44 | [L3Lint.Core](https://www.nuget.org/packages/L3Lint.Core) | 1.0.0 | l3lint contributors | The l3lint engine: canonical commercial card payload model, money and currency… |
| 2026-11-24 04:06:45 | [l3lint](https://www.nuget.org/packages/l3lint) | 1.0.0 | l3lint contributors | l3lint command-line tool: lints commercial card Level 2 and Level 3 payloads ag… |
| 2026-11-24 04:06:46 | [L3Lint.Rules.General](https://www.nuget.org/packages/L3Lint.Rules.General) | 1.0.0 | l3lint contributors | The l3lint general (all brands) rule pack (l3lint.rules.general): versioned, so… |
| 2026-11-24 04:06:47 | [L3Lint.Rules.Discover](https://www.nuget.org/packages/L3Lint.Rules.Discover) | 1.0.0 | l3lint contributors | The l3lint Discover rule pack (l3lint.rules.discover): versioned, sourced rules… |
| 2026-11-24 04:06:48 | [L3Lint.Mcp](https://www.nuget.org/packages/L3Lint.Mcp) | 1.0.0 | l3lint contributors | l3lint MCP server: lets AI agents lint commercial card Level 2 and Level 3 payl… |
| 2026-11-24 04:06:49 | [L3Lint.Hosting](https://www.nuget.org/packages/L3Lint.Hosting) | 1.0.0 | l3lint contributors | l3lint for .NET services: AddL3Lint() registration, configuration loading and b… |
| 2026-11-24 04:06:50 | [L3Lint.Reporting](https://www.nuget.org/packages/L3Lint.Reporting) | 1.0.0 | l3lint contributors | l3lint output writers: text, JSON, SARIF 2.1.0, JUnit XML and Markdown. |
| 2026-11-24 04:06:51 | [L3Lint.Rules.Mastercard](https://www.nuget.org/packages/L3Lint.Rules.Mastercard) | 1.0.0 | l3lint contributors | The l3lint Mastercard rule pack (l3lint.rules.mastercard): versioned, sourced r… |
| 2026-11-24 04:06:51 | [L3Lint.Adapters](https://www.nuget.org/packages/L3Lint.Adapters) | 1.0.0 | l3lint contributors | l3lint input adapters for Stripe, Adyen, Braintree, Cybersource, Authorize.net… |
| 2026-11-24 04:06:52 | [L3Lint.Rules.Visa](https://www.nuget.org/packages/L3Lint.Rules.Visa) | 1.0.0 | l3lint contributors | The l3lint Visa rule pack (l3lint.rules.visa): versioned, sourced rules as YAML… |
| 2026-11-24 04:06:53 | [L3Lint.Rules.Amex](https://www.nuget.org/packages/L3Lint.Rules.Amex) | 1.0.0 | l3lint contributors | The l3lint American Express rule pack (l3lint.rules.amex): versioned, sourced r… |
| 2026-11-24 04:14:57 | [ApiFeatures.Authentications.Users.Cores](https://www.nuget.org/packages/ApiFeatures.Authentications.Users.Cores) | 10.0.0 | Linh Nguyen | Shared user model of the iot-vn Authentication Service: IUser, UserDto, coordin… |
| 2026-11-24 04:15:03 | [ApiFeatures.Authentications.Users.Databases.Mongo](https://www.nuget.org/packages/ApiFeatures.Authentications.Users.Databases.Mongo) | 10.0.0 | Linh Nguyen | MongoDB storage of the iot-vn Authentication Service Users module: registers th… |
| 2026-11-24 04:15:07 | [ApiFeatures.Authentications.Users.Databases.Postgres](https://www.nuget.org/packages/ApiFeatures.Authentications.Users.Databases.Postgres) | 10.0.0 | Linh Nguyen | PostgreSQL storage of the iot-vn Authentication Service Users module: registers… |
| 2026-11-24 04:15:10 | [ApiFeatures.Authentications.Users](https://www.nuget.org/packages/ApiFeatures.Authentications.Users) | 10.0.0 | Linh Nguyen | The Users module of the iot-vn Authentication Service: the user endpoints, auth… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
