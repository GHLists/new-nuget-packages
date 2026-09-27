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

## Latest list — 2026-09-27 10:20 UTC

New packages created between 2026-09-27 09:19 UTC and 2026-09-27 10:20 UTC.

[Full CSV](data/new-nuget-packages-2026-09-27T10-20-46-388369Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-09-27 09:28:14 | [Webority.Azure.Telemetry.Functions](https://www.nuget.org/packages/Webority.Azure.Telemetry.Functions) | 0.7.0 | Webority.Azure.Telemetry.Func… | One-call Webority telemetry for an Azure Functions isolated-worker host: the We… |
| 2026-09-27 09:32:45 | [Khefest.Windows](https://www.nuget.org/packages/Khefest.Windows) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:33:26 | [Khefest.Windowing](https://www.nuget.org/packages/Khefest.Windowing) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:33:40 | [Khefest.UI](https://www.nuget.org/packages/Khefest.UI) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:33:55 | [Khefest.Templates](https://www.nuget.org/packages/Khefest.Templates) | 1.6.2 | Aleksandar Ovcharov | Templates for creating 2D and 3D games with the Khefest Game Engine on .NET 10. |
| 2026-09-27 09:34:07 | [Khefest.Input](https://www.nuget.org/packages/Khefest.Input) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:34:23 | [Khefest.Graphics.LowLevel](https://www.nuget.org/packages/Khefest.Graphics.LowLevel) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:34:33 | [Khefest.Graphics](https://www.nuget.org/packages/Khefest.Graphics) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:34:44 | [Khefest.Core](https://www.nuget.org/packages/Khefest.Core) | 1.6.2 | Aleksandar Ovcharov | Package Description |
| 2026-09-27 09:54:19 | [Themia.Payments.TwoCTwoP](https://www.nuget.org/packages/Themia.Payments.TwoCTwoP) | 0.30.0 | Sarawut Phaekuntod | 2C2P PGW 4.3 (Redirect API) adapter for Themia.Payments's IPaymentGateway: JWT-… |
| 2026-09-27 09:54:41 | [Themia.Payments.Beam](https://www.nuget.org/packages/Themia.Payments.Beam) | 0.30.0 | Sarawut Phaekuntod | Beam Checkout adapter for Themia.Payments's IPaymentGateway: QR PromptPay and c… |
| 2026-09-27 09:54:48 | [Themia.Payments](https://www.nuget.org/packages/Themia.Payments) | 0.30.0 | Sarawut Phaekuntod | Provider-agnostic payment collection: create a charge, read its outcome, refund… |
| 2026-09-27 10:14:33 | [Jev.DotNet](https://www.nuget.org/packages/Jev.DotNet) | 0.1.0 | Burak Altin | Unofficial .NET client for TypeSafe's Jev System One model: ask Noul, Choice, a… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
