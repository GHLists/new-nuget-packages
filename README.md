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

## Latest list — 2026-11-04 12:21 UTC

New packages created between 2026-11-04 09:21 UTC and 2026-11-04 12:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-04T12-21-58-757819Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-04 09:22:46 | [SecurityBuilder](https://www.nuget.org/packages/SecurityBuilder) | 1.0.1 | Khalil.dev | Role-based access control on resources plus field-level access control. The cor… |
| 2026-11-04 09:24:55 | [CsVerify](https://www.nuget.org/packages/CsVerify) | 0.1.0 | Artyom Shalkhakov | ATS-style specifications for C#: contracts, ghost values, linear views. Ships t… |
| 2026-11-04 09:25:07 | [Nullean.Entities.EntityFrameworkCore](https://www.nuget.org/packages/Nullean.Entities.EntityFrameworkCore) | 0.3.0 | Nullean and contributors | Checks Nullean.Entities constraint sets on SaveChanges: added entities are vali… |
| 2026-11-04 09:25:08 | [Nullean.Entities.Blazor](https://www.nuget.org/packages/Nullean.Entities.Blazor) | 0.3.0 | Nullean and contributors | A Blazor EditForm validator that checks the form model against its Nullean.Enti… |
| 2026-11-04 09:25:09 | [Nullean.Entities.SystemCommandLine](https://www.nuget.org/packages/Nullean.Entities.SystemCommandLine) | 0.3.0 | Nullean and contributors | Validates the options a System.CommandLine command binds against Nullean.Entiti… |
| 2026-11-04 09:25:09 | [Nullean.Entities.FluentValidation](https://www.nuget.org/packages/Nullean.Entities.FluentValidation) | 0.3.0 | Nullean and contributors | Bridges Nullean.Entities constraints and FluentValidation both ways: a constrai… |
| 2026-11-04 09:25:10 | [Nullean.Entities.Diagnostics](https://www.nuget.org/packages/Nullean.Entities.Diagnostics) | 0.3.0 | Nullean and contributors | Turns Nullean.Entities violations seen at runtime (rejected changes, missed tem… |
| 2026-11-04 09:25:11 | [Nullean.Entities.ComponentModel](https://www.nuget.org/packages/Nullean.Entities.ComponentModel) | 0.3.0 | Nullean and contributors | Surfaces Nullean.Entities constraint violations through INotifyDataErrorInfo, s… |
| 2026-11-04 09:25:12 | [Nullean.Entities.ReactiveUI](https://www.nuget.org/packages/Nullean.Entities.ReactiveUI) | 0.3.0 | Nullean and contributors | Turns a Nullean.Entities constraint set into ReactiveUI.Validation rules on a v… |
| 2026-11-04 09:25:27 | [dotnet-csverify](https://www.nuget.org/packages/dotnet-csverify) | 0.1.0 | Artyom Shalkhakov | The CsVerify verifier: proves C# code's CsVerify specifications (contracts, loo… |
| 2026-11-04 09:37:59 | [MakeenPay.Shared](https://www.nuget.org/packages/MakeenPay.Shared) | 1.1.0 | MakeenPay | Shared libraries for MakeenPay microservices |
| 2026-11-04 09:39:16 | [SecurityBuilder.AspNetCore](https://www.nuget.org/packages/SecurityBuilder.AspNetCore) | 1.0.1 | Khalil.dev | Wires SecurityBuilder into ASP.NET Core: dependency injection, the middleware t… |
| 2026-11-04 09:39:31 | [SecurityBuilder.EntityFrameworkCore](https://www.nuget.org/packages/SecurityBuilder.EntityFrameworkCore) | 1.0.1 | Khalil.dev | Applies SecurityBuilder to plain EF Core: hidden fields come back null in proje… |
| 2026-11-04 09:39:44 | [SecurityBuilder.Identity](https://www.nuget.org/packages/SecurityBuilder.Identity) | 1.0.1 | Khalil.dev | Optional users and tokens for SecurityBuilder: accounts with hashed passwords,… |
| 2026-11-04 09:42:16 | [BSynchro.Notification.Public](https://www.nuget.org/packages/BSynchro.Notification.Public) | 8.4.0 | BSynchro | Client for the notification service: template DTOs, INotificationClient and Add… |
| 2026-11-04 09:48:45 | [DevToys.Totp](https://www.nuget.org/packages/DevToys.Totp) | 1.0.1 | DevToys.Totp contributors | Offline 2FA / TOTP code generator for DevToys 2. Supports Base32 secrets, otpau… |
| 2026-11-04 09:55:12 | [Hostpanel.Sdk](https://www.nuget.org/packages/Hostpanel.Sdk) | 3.0.0 | Hostpanel contributors | Plugin contracts for hostpanel: provisioning, payment, registrar, identity, ful… |
| 2026-11-04 10:01:08 | [Umbraco.Community.LogLevels](https://www.nuget.org/packages/Umbraco.Community.LogLevels) | 17.0.0-rc1 | skttl | Change Serilog log levels and namespace overrides at runtime from the Umbraco L… |
| 2026-11-04 10:18:05 | [Plugin.Maui.Spine.Symbols.Tool](https://www.nuget.org/packages/Plugin.Maui.Spine.Symbols.Tool) | 0.1.40 | Jonatan Söderberg | The spine-symbols command: turns SVG icons into custom symbols for an iOS asset… |
| 2026-11-04 10:19:45 | [SimdSkia](https://www.nuget.org/packages/SimdSkia) | 0.1.0 | hnlyf168 | SimdSkia convenience package for the documented SkiaSharp namespace source comp… |
| 2026-11-04 10:19:46 | [SimdSkia.Avalonia](https://www.nuget.org/packages/SimdSkia.Avalonia) | 0.1.0 | hnlyf168 | Managed C# rendering/font services for Avalonia 12.1.5. Windows/Linux/macOS ins… |
| 2026-11-04 10:19:47 | [SimdSkia.Avalonia.Desktop](https://www.nuget.org/packages/SimdSkia.Avalonia.Desktop) | 0.1.0 | hnlyf168 | Preview Windows, Linux X11 and macOS software window hosts for SimdSkia. macOS… |
| 2026-11-04 10:19:48 | [SimdSkia.Avalonia.Gpu](https://www.nuget.org/packages/SimdSkia.Avalonia.Gpu) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:49 | [SimdSkia.Compatibility](https://www.nuget.org/packages/SimdSkia.Compatibility) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:50 | [SimdSkia.Core](https://www.nuget.org/packages/SimdSkia.Core) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:51 | [SimdSkia.Cpu](https://www.nuget.org/packages/SimdSkia.Cpu) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:52 | [SimdSkia.Gpu](https://www.nuget.org/packages/SimdSkia.Gpu) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:53 | [SimdSkia.Gpu.Direct2D](https://www.nuget.org/packages/SimdSkia.Gpu.Direct2D) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:54 | [SimdSkia.Imaging](https://www.nuget.org/packages/SimdSkia.Imaging) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:19:55 | [SimdSkia.Pdf](https://www.nuget.org/packages/SimdSkia.Pdf) | 0.1.0 | hnlyf168 | Optional pure managed PDF parsing and SimdSkia page rendering. Supported PDF fe… |
| 2026-11-04 10:19:56 | [SimdSkia.Text](https://www.nuget.org/packages/SimdSkia.Text) | 0.1.0 | hnlyf168 | Managed C# 2D rendering components. Version 0.1 supports the documented subset;… |
| 2026-11-04 10:25:01 | [BccCode.Hailey.Client](https://www.nuget.org/packages/BccCode.Hailey.Client) | 1.0.0.14 | BccCode.Hailey.Client | .Net SDK for the Hailey API |
| 2026-11-04 10:27:33 | [Umbraco.Community.SmtpOAuthMailSender](https://www.nuget.org/packages/Umbraco.Community.SmtpOAuthMailSender) | 18.0.0-rc1 | skttl | SMTP OAuth email delivery for Umbraco, configured through existing SMTP setting… |
| 2026-11-04 10:27:38 | [Umbraco.Community.Messenger](https://www.nuget.org/packages/Umbraco.Community.Messenger) | 18.0.0-rc1 | skttl | Internal threaded messaging for Umbraco backoffice users. |
| 2026-11-04 10:27:46 | [Umbraco.Community.Handbook](https://www.nuget.org/packages/Umbraco.Community.Handbook) | 18.0.0-rc1 | skttl | Display your own Markdown documentation inside the Umbraco backoffice. |
| 2026-11-04 10:31:04 | [Umbraco.Community.GraphMailSender](https://www.nuget.org/packages/Umbraco.Community.GraphMailSender) | 18.0.0-rc1 | skttl | Microsoft Graph email delivery for Umbraco, configured through existing SMTP se… |
| 2026-11-04 10:58:26 | [OpenRoam](https://www.nuget.org/packages/OpenRoam) | 0.0.1 | OpenRoam | Placeholder for the official OpenRoam Partner API SDK. The real SDK will be rel… |
| 2026-11-04 10:59:31 | [Sia.Spirv.Workload.Manifest-11.0.100-rc.3](https://www.nuget.org/packages/Sia.Spirv.Workload.Manifest-11.0.100-rc.3) | 0.0.25 | Sia.Spirv.Workload.Manifest | Workload manifest for the Sia LLVM SPIR-V toolchain. |
| 2026-11-04 11:26:23 | [RazorKit.TomSelect](https://www.nuget.org/packages/RazorKit.TomSelect) | 2.1.1 | Emrah KONDUR | Fluent Razor HTML helpers for Tom Select, including model binding, remote data,… |
| 2026-11-04 11:30:17 | [Cutaway.BackgroundRemoval](https://www.nuget.org/packages/Cutaway.BackgroundRemoval) | 0.3.0-beta | Cormier Solutions LLC | Server-side colour flood fill and opt-in U2-Net-p photo background removal for… |
| 2026-11-04 11:31:00 | [Webority.Social.Inbox](https://www.nuget.org/packages/Webority.Social.Inbox) | 0.14.0 | Webority Technologies | Comments, mentions, reviews and replies for Webority.Social: reads the replies… |
| 2026-11-04 11:31:10 | [Webority.Social.Cards.Carousel](https://www.nuget.org/packages/Webority.Social.Cards.Carousel) | 0.14.0 | Webority Technologies | Carousel and document cards for Webority.Social.Cards: draws a brand-skinned sl… |
| 2026-11-04 11:31:12 | [Webority.Social.Diagnostics](https://www.nuget.org/packages/Webority.Social.Diagnostics) | 0.14.0 | Webority Technologies | Pipeline health for Webority.Social in the Webority Diagnostics console: one co… |
| 2026-11-04 11:31:27 | [Mafesoft.Maui.AdvancedWebView](https://www.nuget.org/packages/Mafesoft.Maui.AdvancedWebView) | 1.0.0 | Federico Mazzanti | AdvancedWebView is a lightweight WebView for .NET MAUI (Android and iOS) that e… |
| 2026-11-04 11:32:39 | [Qedra](https://www.nuget.org/packages/Qedra) | 1.109.7.11 | Evgeniy Veprikov | Computer algebra with verifiable answers: integrals, limits, sums, ODEs |
| 2026-11-04 11:46:03 | [ToolUp.Platform.Server.Audit](https://www.nuget.org/packages/ToolUp.Platform.Server.Audit) | 0.39.0 | Andrew J. Willshire | ToolUp.Platform server tier, Audit part: the audit log and its replication, art… |
| 2026-11-04 11:46:04 | [ToolUp.Platform.Server.Config](https://www.nuget.org/packages/ToolUp.Platform.Server.Config) | 0.39.0 | Andrew J. Willshire | ToolUp.Platform server tier, Config part: configuration resolution and the envi… |
| 2026-11-04 11:46:05 | [ToolUp.Platform.Server.Infra](https://www.nuget.org/packages/ToolUp.Platform.Server.Infra) | 0.39.0 | Andrew J. Willshire | ToolUp.Platform server tier, Infra part: the substrate the subsystems stand on… |
| 2026-11-04 11:46:06 | [ToolUp.Platform.Server.Jobs](https://www.nuget.org/packages/ToolUp.Platform.Server.Jobs) | 0.39.0 | Andrew J. Willshire | ToolUp.Platform server tier, Jobs part: the job store and scheduler, notificati… |
| 2026-11-04 11:46:07 | [ToolUp.Platform.Server.Remoting](https://www.nuget.org/packages/ToolUp.Platform.Server.Remoting) | 0.39.0 | Andrew J. Willshire | ToolUp.Platform server tier, Remoting part: the remoting transport (the Message… |
| 2026-11-04 11:46:07 | [ToolUp.Platform.Server.Scope](https://www.nuget.org/packages/ToolUp.Platform.Server.Scope) | 0.39.0 | Andrew J. Willshire | ToolUp.Platform server tier, Scope part: scope resolution, teams and invitation… |
| 2026-11-04 11:49:11 | [EFCore.MaterializR](https://www.nuget.org/packages/EFCore.MaterializR) | 1.0.0 | Adam O'Neil | EF Core-based incremental cache updates |
| 2026-11-04 11:50:02 | [Juice.Observability.Rules](https://www.nuget.org/packages/Juice.Observability.Rules) | 1.0.0 | Creatorflow.io | Juice Observability: discovery, health, rules and alerts over OpenTelemetry for… |
| 2026-11-04 11:50:02 | [Juice.Observability.Data](https://www.nuget.org/packages/Juice.Observability.Data) | 1.0.0 | Creatorflow.io | Juice Observability: discovery, health, rules and alerts over OpenTelemetry for… |
| 2026-11-04 11:50:03 | [Juice.Observability.Discovery](https://www.nuget.org/packages/Juice.Observability.Discovery) | 1.0.0 | Creatorflow.io | Juice Observability: discovery, health, rules and alerts over OpenTelemetry for… |
| 2026-11-04 11:50:03 | [Juice.Observability.Webhooks](https://www.nuget.org/packages/Juice.Observability.Webhooks) | 1.0.0 | Creatorflow.io | Juice Observability: discovery, health, rules and alerts over OpenTelemetry for… |
| 2026-11-04 11:50:04 | [Juice.Observability.Health](https://www.nuget.org/packages/Juice.Observability.Health) | 1.0.0 | Creatorflow.io | Juice Observability: discovery, health, rules and alerts over OpenTelemetry for… |
| 2026-11-04 11:50:04 | [Juice.Observability.Api](https://www.nuget.org/packages/Juice.Observability.Api) | 1.0.0 | Creatorflow.io | Juice Observability platform API (/api/v1) and its discovery, health, rule and… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
