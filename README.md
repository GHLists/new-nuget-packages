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

## Latest list — 2026-11-05 05:20 UTC

New packages created between 2026-11-05 04:21 UTC and 2026-11-05 05:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-05T05-20-22-662506Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-05 04:31:50 | [AppWeaver.Security.Store](https://www.nuget.org/packages/AppWeaver.Security.Store) | 1.0.0 | Team AppWeaver | AppWeaver Security store abstraction: permission catalog and role-permission ma… |
| 2026-11-05 04:32:18 | [Iso20022Kit.Cli](https://www.nuget.org/packages/Iso20022Kit.Cli) | 0.1.0 | Vong Visalsambath | Command-line tool: validate and read ISO 20022 pacs.008 and camt.053 messages,… |
| 2026-11-05 04:32:19 | [Iso20022Kit](https://www.nuget.org/packages/Iso20022Kit) | 0.1.0 | Vong Visalsambath | Read, write and validate ISO 20022 payment messages (pacs.008 customer credit t… |
| 2026-11-05 04:33:44 | [SlaClock](https://www.nuget.org/packages/SlaClock) | 0.1.0 | Vong Visalsambath | Business-hours deadlines and pausable SLA timers for .NET. Weekly hours with sp… |
| 2026-11-05 04:34:01 | [Amortizer.Cli](https://www.nuget.org/packages/Amortizer.Cli) | 0.1.0 | Vong Visalsambath | Command-line loan schedules: payments, interest, APR and the true cost of flat-… |
| 2026-11-05 04:34:02 | [Amortizer](https://www.nuget.org/packages/Amortizer) | 0.1.0 | Vong Visalsambath | Loan schedules done exactly in .NET: annuity, equal-principal, interest-only an… |
| 2026-11-05 04:34:11 | [TxMonitor.Cli](https://www.nuget.org/packages/TxMonitor.Cli) | 0.1.0 | Vong Visalsambath | Run transaction monitoring rules over a CSV of transactions and get explained a… |
| 2026-11-05 04:34:11 | [Iso8583Kit.Cli](https://www.nuget.org/packages/Iso8583Kit.Cli) | 0.1.0 | Vong Visalsambath | Read, build and send ISO 8583 messages, and run a simulated card host for testi… |
| 2026-11-05 04:34:11 | [TxMonitor](https://www.nuget.org/packages/TxMonitor) | 0.1.0 | Vong Visalsambath | A transaction monitoring rules engine for anti-money-laundering alerts: structu… |
| 2026-11-05 04:34:12 | [Iso8583Kit](https://www.nuget.org/packages/Iso8583Kit) | 0.1.0 | Vong Visalsambath | Read, write, check and explain ISO 8583 card messages (1987): ASCII and binary/… |
| 2026-11-05 04:34:24 | [SanctionScreen](https://www.nuget.org/packages/SanctionScreen) | 0.1.0 | Vong Visalsambath | Screen names against OFAC's public Specially Designated Nationals (SDN) list: f… |
| 2026-11-05 04:34:24 | [SanctionScreen.Cli](https://www.nuget.org/packages/SanctionScreen.Cli) | 0.1.0 | Vong Visalsambath | Screen names against the OFAC SDN list from the command line, one at a time or… |
| 2026-11-05 04:34:30 | [LedgerKit.PostgreSql](https://www.nuget.org/packages/LedgerKit.PostgreSql) | 0.1.0 | Vong Visalsambath | PostgreSQL storage for LedgerKit. The database itself refuses unbalanced entrie… |
| 2026-11-05 04:34:31 | [LedgerKit.Cli](https://www.nuget.org/packages/LedgerKit.Cli) | 0.1.0 | Vong Visalsambath | Post to a double-entry ledger and reconcile it with ISO 20022 camt.053 bank sta… |
| 2026-11-05 04:34:32 | [LedgerKit](https://www.nuget.org/packages/LedgerKit) | 0.1.0 | Vong Visalsambath | A double-entry ledger that refuses unbalanced or edited entries, and bank recon… |
| 2026-11-05 04:48:24 | [Cangming.Toolkit.Avalonias.AtomUI](https://www.nuget.org/packages/Cangming.Toolkit.Avalonias.AtomUI) | 0.1.5.1105 | Fangyu,lukan@xknife.net,Asong… | 仅组织内部使用。基于 AtomUI 的启动接入、主题切换与对话框实现。 |
| 2026-11-05 04:50:36 | [Maple.Result.Extensions.Functions.Worker.AspNetCore](https://www.nuget.org/packages/Maple.Result.Extensions.Functions.Worker.AspNetCore) | 0.15.0 | Tom Maple | Provides mapping of the Maple.Result to the ASP.NET Core ActionResult in Azure… |
| 2026-11-05 05:09:23 | [AppWeaver.Tenancy](https://www.nuget.org/packages/AppWeaver.Tenancy) | 1.0.0 | Team AppWeaver | AppWeaver Tenancy Abstractions Library in AppWeaver framework. |
| 2026-11-05 05:13:29 | [AppWeaver.Tenancy.EfCore](https://www.nuget.org/packages/AppWeaver.Tenancy.EfCore) | 1.0.0 | Team AppWeaver | EF Core provider implementation for AppWeaver.Tenancy. Provider-agnostic ITenan… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
