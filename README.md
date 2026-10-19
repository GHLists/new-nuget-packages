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

## Latest list — 2026-10-19 04:20 UTC

New packages created between 2026-10-19 03:21 UTC and 2026-10-19 04:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-19T04-20-19-267222Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-19 03:30:57 | [LINGYUN.Abp.Aliyun.Captcha](https://www.nuget.org/packages/LINGYUN.Abp.Aliyun.Captcha) | 10.7.0 | colin | 阿里云验证码服务Abp集成 |
| 2026-10-19 03:31:02 | [LINGYUN.Abp.AspNetCore.Authentication](https://www.nuget.org/packages/LINGYUN.Abp.AspNetCore.Authentication) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:31:51 | [LINGYUN.Abp.AuditLogging.OpenObserve](https://www.nuget.org/packages/LINGYUN.Abp.AuditLogging.OpenObserve) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:37:54 | [LINGYUN.Abp.Logging.Serilog.OpenObserve](https://www.nuget.org/packages/LINGYUN.Abp.Logging.Serilog.OpenObserve) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:37:57 | [LINGYUN.Abp.MaxMindGeoIP2](https://www.nuget.org/packages/LINGYUN.Abp.MaxMindGeoIP2) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:38:14 | [LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore](https://www.nuget.org/packages/LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:38:17 | [LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore.MySql](https://www.nuget.org/packages/LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore.MySql) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:38:20 | [LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore.PostgreSql](https://www.nuget.org/packages/LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore.PostgreSql) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:38:23 | [LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore.SqlServer](https://www.nuget.org/packages/LINGYUN.Abp.MicroService.AllInOne.EntityFrameworkCore.SqlServer) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:39:49 | [LINGYUN.Abp.OpenObserve](https://www.nuget.org/packages/LINGYUN.Abp.OpenObserve) | 10.7.0 | colin | Package Description |
| 2026-10-19 03:41:51 | [LINGYUN.Abp.Tencent.Captcha](https://www.nuget.org/packages/LINGYUN.Abp.Tencent.Captcha) | 10.7.0 | colin | 腾讯云验证码服务Abp集成 |
| 2026-10-19 04:08:16 | [FlexRule.Extensions.Authenticator](https://www.nuget.org/packages/FlexRule.Extensions.Authenticator) | 11.4.2086 | Pliant Framework - FlexRule | Introduces additional authentication Functionality |
| 2026-10-19 04:09:19 | [DotNetCore.Lutter.Extensions.OpenTelemetry](https://www.nuget.org/packages/DotNetCore.Lutter.Extensions.OpenTelemetry) | 3.1.0 | AlexLEWIS | OpenTelemetry wiring for the DotNetCore.Lutter resilience kernel. Registers the… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
