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

## Latest list — 2026-10-03 19:21 UTC

New packages created between 2026-10-03 18:20 UTC and 2026-10-03 19:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-03T19-21-56-441024Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-03 18:23:07 | [Authorizer.GrpcCommon](https://www.nuget.org/packages/Authorizer.GrpcCommon) | 10.0.4 | Joseph Melberg | Package Description |
| 2026-10-03 18:23:08 | [Authorizer.Domain](https://www.nuget.org/packages/Authorizer.Domain) | 10.0.4 | Joseph Melberg | Package Description |
| 2026-10-03 18:23:08 | [Authorizer.GrpcClient](https://www.nuget.org/packages/Authorizer.GrpcClient) | 10.0.4 | Joseph Melberg | Package Description |
| 2026-10-03 18:23:23 | [Alethic.Node](https://www.nuget.org/packages/Alethic.Node) | 1.0.0 | Jerome Haltom | Node embedded in a .NET process through node-api-dotnet: a pool of engines, eac… |
| 2026-10-03 18:23:24 | [Alethic.Node.AspNet](https://www.nuget.org/packages/Alethic.Node.AspNet) | 1.0.0 | Jerome Haltom | Node embedded in an ASP.NET (System.Web) application on .NET Framework, over Al… |
| 2026-10-03 18:23:24 | [Alethic.Node.AspNet.Components](https://www.nuget.org/packages/Alethic.Node.AspNet.Components) | 1.0.0 | Jerome Haltom | JavaScript components hosted on ASP.NET Web Forms pages: a Component control wh… |
| 2026-10-03 18:23:24 | [Alethic.Node.AspNetCore](https://www.nuget.org/packages/Alethic.Node.AspNetCore) | 1.0.0 | Jerome Haltom | Server-side rendering for ASP.NET Core on a Node runtime embedded in the proces… |
| 2026-10-03 18:23:25 | [Alethic.Node.Http](https://www.nuget.org/packages/Alethic.Node.Http) | 1.0.0 | Jerome Haltom | Serving a JavaScript application over HTTP from Node embedded in a .NET process… |
| 2026-10-03 18:42:42 | [Fwd.Umbraco.WelcomePage](https://www.nuget.org/packages/Fwd.Umbraco.WelcomePage) | 17.0.5 | FWD Motion | Displays the private Flex client news feed in the Umbraco Content dashboard. |
| 2026-10-03 18:49:50 | [SmsProNikita](https://www.nuget.org/packages/SmsProNikita) | 1.0.1 | taalaibekdev | DI-клиент для XML-протокола SMS-шлюза smspro.nikita.kg (отправка SMS, отчёты о… |
| 2026-10-03 19:00:21 | [Zen.Logging.Standard](https://www.nuget.org/packages/Zen.Logging.Standard) | 1.0.9 | Zen.Logging.Standard | Package Description |
| 2026-10-03 19:10:13 | [InterMW.Authorizer.GrpcCommon](https://www.nuget.org/packages/InterMW.Authorizer.GrpcCommon) | 10.0.11 | Joseph Melberg | Package Description |
| 2026-10-03 19:10:14 | [InterMW.Authorizer.Domain](https://www.nuget.org/packages/InterMW.Authorizer.Domain) | 10.0.11 | Joseph Melberg | Package Description |
| 2026-10-03 19:10:14 | [InterMW.Authorizer.GrpcClient](https://www.nuget.org/packages/InterMW.Authorizer.GrpcClient) | 10.0.11 | Joseph Melberg | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
