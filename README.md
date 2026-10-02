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

## Latest list — 2026-10-02 07:21 UTC

New packages created between 2026-10-02 06:20 UTC and 2026-10-02 07:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-02T07-21-14-166969Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-02 06:30:10 | [Rony.Net.NUnit](https://www.nuget.org/packages/Rony.Net.NUnit) | 1.1.0 | Mojtaba Kiani | NUnit integration for Rony.Net: a MockServerTest base class that starts a mock… |
| 2026-10-02 06:30:11 | [Rony.Net.Xunit](https://www.nuget.org/packages/Rony.Net.Xunit) | 1.1.0 | Mojtaba Kiani | xUnit (v2) integration for Rony.Net: a MockServerTest base class that starts a… |
| 2026-10-02 06:30:11 | [Rony.Net.MSTest](https://www.nuget.org/packages/Rony.Net.MSTest) | 1.1.0 | Mojtaba Kiani | MSTest (v4) integration for Rony.Net: a MockServerTest base class that starts a… |
| 2026-10-02 07:01:30 | [SqlWright.DynamicQuery](https://www.nuget.org/packages/SqlWright.DynamicQuery) | 1.0.0 | Vishram Singh | Safe, allowlisted dynamic queries for SqlWright: turn a JSON query request (fil… |
| 2026-10-02 07:01:30 | [SqlWright](https://www.nuget.org/packages/SqlWright) | 1.0.0 | Vishram Singh | A fast, lightweight micro-ORM for .NET. Injection-safe interpolated SQL, built-… |
| 2026-10-02 07:15:34 | [TechTeaStudio.Auth.OAuth.Microsoft](https://www.nuget.org/packages/TechTeaStudio.Auth.OAuth.Microsoft) | 0.11.1 | Ronald Ryan | Microsoft Entra ID (Azure AD) OAuth 2.0 / OIDC provider for TechTeaStudio.Auth… |
| 2026-10-02 07:15:36 | [TechTeaStudio.Auth.Providers.Telegram](https://www.nuget.org/packages/TechTeaStudio.Auth.Providers.Telegram) | 0.11.1 | Ronald Ryan | Telegram Login Widget sign-in for TechTeaStudio.Auth. Not OAuth: Telegram signs… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
