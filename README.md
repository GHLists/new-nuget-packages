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

## Latest list — 2026-10-30 19:21 UTC

New packages created between 2026-10-30 18:21 UTC and 2026-10-30 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-30T19-21-03-622784Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-30 18:24:25 | [Pleiades.Core](https://www.nuget.org/packages/Pleiades.Core) | 3.0.1 | Daniele Fusi | Package Description |
| 2026-10-30 18:24:28 | [CFITS.Generator](https://www.nuget.org/packages/CFITS.Generator) | 0.1.0 | MPSQUARK | Source generator for strongly typed CFITS serializer contexts. |
| 2026-10-30 18:24:28 | [Pleiades.Ef](https://www.nuget.org/packages/Pleiades.Ef) | 3.0.1 | Daniele Fusi | Package Description |
| 2026-10-30 18:24:31 | [Pleiades.Index](https://www.nuget.org/packages/Pleiades.Index) | 3.0.1 | Pleiades.Index | Package Description |
| 2026-10-30 18:24:35 | [Pleiades.Ef.PgSql](https://www.nuget.org/packages/Pleiades.Ef.PgSql) | 3.0.1 | Pleiades.Ef.PgSql | Package Description |
| 2026-10-30 18:24:38 | [Pleiades.Geo](https://www.nuget.org/packages/Pleiades.Geo) | 3.0.1 | Daniele Fusi | Package Description |
| 2026-10-30 18:24:41 | [Pleiades.Migration](https://www.nuget.org/packages/Pleiades.Migration) | 3.0.1 | Daniele Fusi | Package Description |
| 2026-10-30 18:24:45 | [Pleiades.Search](https://www.nuget.org/packages/Pleiades.Search) | 3.0.1 | Pleiades.Search | Package Description |
| 2026-10-30 18:24:48 | [Pleiades.Search.PgSql](https://www.nuget.org/packages/Pleiades.Search.PgSql) | 3.0.1 | Pleiades.Search.PgSql | Package Description |
| 2026-10-30 18:30:23 | [GM.Secrets.AwsSecretsManager](https://www.nuget.org/packages/GM.Secrets.AwsSecretsManager) | 2.0.0 | Giorgi Metskhvarishvili | AWS Secrets Manager provider for GM.Secrets — reads the configured secrets (a J… |
| 2026-10-30 18:30:24 | [GM.Secrets.Doppler](https://www.nuget.org/packages/GM.Secrets.Doppler) | 2.0.0 | Giorgi Metskhvarishvili | Doppler store for GM.Secrets — downloads a Doppler config's secrets (REST API,… |
| 2026-10-30 18:30:25 | [GM.Secrets.Vault](https://www.nuget.org/packages/GM.Secrets.Vault) | 2.0.0 | Giorgi Metskhvarishvili | HashiCorp Vault secrets provider for GM.Secrets — reads KV v2 paths over Vault'… |
| 2026-10-30 18:30:26 | [GM.Secrets.AzureKeyVault](https://www.nuget.org/packages/GM.Secrets.AzureKeyVault) | 2.0.0 | Giorgi Metskhvarishvili | Azure Key Vault secrets provider for GM.Secrets — loads a vault's enabled secre… |
| 2026-10-30 18:58:52 | [Gobln.Pager.EntityFrameworkCore](https://www.nuget.org/packages/Gobln.Pager.EntityFrameworkCore) | 2.0.0 | Jorn Hendrickx | Asynchronous paging for Entity Framework Core with Gobln.Pager. Makes ToPageAsy… |
| 2026-10-30 18:58:53 | [Gobln.Pager.Json.Newtonsoft](https://www.nuget.org/packages/Gobln.Pager.Json.Newtonsoft) | 2.0.0 | Jorn Hendrickx | Newtonsoft.Json converters for Gobln.Pager. Serializes and deserializes Page an… |
| 2026-10-30 18:58:54 | [Gobln.Pager.Json.Microsoft](https://www.nuget.org/packages/Gobln.Pager.Json.Microsoft) | 2.0.0 | Jorn Hendrickx | System.Text.Json converters for Gobln.Pager. Serializes and deserializes Page a… |
| 2026-10-30 19:15:46 | [FluentCss.Core](https://www.nuget.org/packages/FluentCss.Core) | 0.1.0 | stanac | Fluent strongly typed CSS for Blazor, MVC and Razor Pages |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
