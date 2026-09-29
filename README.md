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

## Latest list — 2026-09-29 12:19 UTC

New packages created between 2026-09-29 11:21 UTC and 2026-09-29 12:19 UTC.

[Full CSV](data/new-nuget-packages-2026-09-29T12-19-17-65401Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-29 11:43:00 | [Simform.Data.Auditing](https://www.nuget.org/packages/Simform.Data.Auditing) | 1.0.0 | Simform Solutions | Automatic, provider-independent audit trails for EF Core 10. Captures Added, Mo… |
| 2026-09-29 11:43:01 | [Simform.Data.Auditing.AspNetCore](https://www.nuget.org/packages/Simform.Data.Auditing.AspNetCore) | 1.0.0 | Simform Solutions | ASP.NET Core integration for Simform.Data.Auditing: resolves the current user f… |
| 2026-09-29 11:45:00 | [Verify.Cecil](https://www.nuget.org/packages/Verify.Cecil) | 0.1.0 | https://github.com/VerifyTest… | Extends Verify (https://github.com/VerifyTests/Verify) to allow snapshot testin… |
| 2026-09-29 11:45:00 | [Verify.Cecil.FodyHelpers](https://www.nuget.org/packages/Verify.Cecil.FodyHelpers) | 0.1.0 | https://github.com/VerifyTest… | Extends Verify (https://github.com/VerifyTests/Verify) to allow snapshot testin… |
| 2026-09-29 11:46:29 | [getAddress.Dk.Sdk](https://www.nuget.org/packages/getAddress.Dk.Sdk) | 1.0.0 | getAddress() | .NET client for getaddress.dk, the DAWA-compatible Danish address API: autocomp… |
| 2026-09-29 11:54:25 | [Majorsilence.Forms.Theming.Avalonia](https://www.nuget.org/packages/Majorsilence.Forms.Theming.Avalonia) | 26.4.0 | Majorsilence | Applies Majorsilence.Forms CSS themes to native Avalonia controls — one stylesh… |
| 2026-09-29 11:54:26 | [Majorsilence.Forms.Mvvm](https://www.nuget.org/packages/Majorsilence.Forms.Mvvm) | 26.4.0 | Majorsilence | Trim- and AOT-safe MVVM wiring for Majorsilence.Forms: Observe, BindCommand and… |
| 2026-09-29 11:55:26 | [Arc56.Generated.TriplEight.AuPM](https://www.nuget.org/packages/Arc56.Generated.TriplEight.AuPM) | 1.0.1.2026092911 | TriplEight | Generated ARC-56 Algorand smart-contract clients for TriplEight/AuPM. |
| 2026-09-29 11:58:49 | [Umai.KeycloakService.Contract.Grpc](https://www.nuget.org/packages/Umai.KeycloakService.Contract.Grpc) | 1.0.0 | Umai.KeycloakService.Contract… | Code-first gRPC контракт umai-keycloak-service: зеркало пользователей Keycloak… |
| 2026-09-29 11:59:35 | [Umai.KeycloakService.Contract](https://www.nuget.org/packages/Umai.KeycloakService.Contract) | 1.0.0 | Umai.KeycloakService.Contract | Сообщения RabbitMQ (MassTransit), публикуемые umai-keycloak-service при изменен… |
| 2026-09-29 12:09:57 | [Mandarin.Selenium](https://www.nuget.org/packages/Mandarin.Selenium) | 0.1.0 | Mandarin | Selenium for Mandarin .NET services: one-line DI registration (AddMandarinSelen… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
