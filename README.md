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

## Latest list — 2026-10-23 19:20 UTC

New packages created between 2026-10-23 18:20 UTC and 2026-10-23 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-23T19-20-26-324353Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-23 18:23:03 | [WebSvc.PayLink.Abstractions](https://www.nuget.org/packages/WebSvc.PayLink.Abstractions) | 0.3.0 | WebSvc | Contracts for PayLink payment connectors: manifest, configuration schema, attem… |
| 2026-10-23 18:23:05 | [WebSvc.PayLink.Connector.CCAvenue](https://www.nuget.org/packages/WebSvc.PayLink.Connector.CCAvenue) | 0.1.0 | WebSvc | CCAvenue for PayLink: encrypted (AES) hosted checkout, order status tracker and… |
| 2026-10-23 18:23:08 | [WebSvc.PayLink.Connector.PayPal](https://www.nuget.org/packages/WebSvc.PayLink.Connector.PayPal) | 0.1.0 | WebSvc | PayPal for PayLink: Orders v2 checkout with capture on return, verified webhook… |
| 2026-10-23 18:23:10 | [WebSvc.PayLink.Connector.PayU](https://www.nuget.org/packages/WebSvc.PayLink.Connector.PayU) | 0.1.0 | WebSvc | PayU for PayLink: hosted checkout by form post with SHA-512 hashes, verify_paym… |
| 2026-10-23 18:23:12 | [WebSvc.PayLink.Connector.PhonePe](https://www.nuget.org/packages/WebSvc.PayLink.Connector.PhonePe) | 0.1.0 | WebSvc | PhonePe for PayLink: Standard Checkout v2 (OAuth) or the older salt-key API, st… |
| 2026-10-23 18:23:15 | [WebSvc.PayLink.Connector.Razorpay](https://www.nuget.org/packages/WebSvc.PayLink.Connector.Razorpay) | 0.2.0 | WebSvc | Razorpay for PayLink: Payment Links checkout, signed callbacks and webhooks, st… |
| 2026-10-23 18:23:17 | [WebSvc.PayLink.Connector.Simulator](https://www.nuget.org/packages/WebSvc.PayLink.Connector.Simulator) | 0.1.0 | WebSvc | PayLink's built-in test connector: the checkout offers Succeed, Fail and Stay p… |
| 2026-10-23 18:23:19 | [WebSvc.PayLink.Connector.Stripe](https://www.nuget.org/packages/WebSvc.PayLink.Connector.Stripe) | 0.1.0 | WebSvc | Stripe for PayLink: Checkout Sessions, signed webhooks, status checks, refunds… |
| 2026-10-23 18:23:22 | [WebSvc.PayLink.Connector.Upi](https://www.nuget.org/packages/WebSvc.PayLink.Connector.Upi) | 0.1.0 | WebSvc | PayLink UPI: a free method that shows a upi://pay QR code paying straight to th… |
| 2026-10-23 18:23:24 | [WebSvc.PayLink.Storage](https://www.nuget.org/packages/WebSvc.PayLink.Storage) | 0.5.0 | WebSvc | Engine-neutral storage for PayLink: SQLite, MySQL and PostgreSQL connections, S… |
| 2026-10-23 18:30:27 | [NORM.CorrelationId](https://www.nuget.org/packages/NORM.CorrelationId) | 1.0.3 | İlhan Enes Daniş | Lightweight, allocation-conscious correlation ID primitives for .NET 6 through… |
| 2026-10-23 18:30:29 | [NORM.CorrelationId.AspNetCore](https://www.nuget.org/packages/NORM.CorrelationId.AspNetCore) | 1.0.3 | İlhan Enes Daniş | ASP.NET Core middleware for NORM.CorrelationId (.NET 6 - .NET 10): reads, valid… |
| 2026-10-23 18:33:48 | [Samabase.Data.OracleClient](https://www.nuget.org/packages/Samabase.Data.OracleClient) | 10.0.2 | Samabase | General purpose OracleClient library that allows you to communicate with Oracle… |
| 2026-10-23 18:35:22 | [Samabase.Data.OracleRepositories](https://www.nuget.org/packages/Samabase.Data.OracleRepositories) | 1.9.2 | Samabase | General purpose OracleRepositories library that allows you to communicate with… |
| 2026-10-23 18:40:44 | [BeneficialStrategies.Iso20022.Messages.Samples](https://www.nuget.org/packages/BeneficialStrategies.Iso20022.Messages.Samples) | 1.0.0-alpha | Jeff Ward,Beneficial Strategi… | Named, valid ISO 20022 objects for tests, and a generated minimal valid object… |
| 2026-10-23 18:58:10 | [Cesium.Net](https://www.nuget.org/packages/Cesium.Net) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Cesium.Net core: a host-agnostic .NET API for CesiumJS (3D globes, maps, terrai… |
| 2026-10-23 18:58:10 | [Cesium.Net.Blazor](https://www.nuget.org/packages/Cesium.Net.Blazor) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Blazor components for Cesium.Net — embed a CesiumJS 3D globe/map in Blazor Serv… |
| 2026-10-23 18:58:11 | [Cesium.Net.Avalonia](https://www.nuget.org/packages/Cesium.Net.Avalonia) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Avalonia UI control for Cesium.Net — a native-WebView hosted CesiumJS 3D globe/… |
| 2026-10-23 19:03:34 | [Cratis.Screenplay.Matching](https://www.nuget.org/packages/Cratis.Screenplay.Matching) | 4.241.0 | Cratis | Portable linear-time pattern matching for Screenplay applications |
| 2026-10-23 19:05:27 | [Oracle.ManagedDataAccess.SQLScriptExecution](https://www.nuget.org/packages/Oracle.ManagedDataAccess.SQLScriptExecution) | 23.26.400 | Oracle | This NuGet package supports .SQL Script Execution for ODP.NET Core. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
