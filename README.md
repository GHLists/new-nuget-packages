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

## Latest list — 2026-10-21 01:20 UTC

New packages created between 2026-10-21 00:21 UTC and 2026-10-21 01:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-21T01-20-14-983746Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-21 00:48:06 | [heirowDebug.ProjectZ](https://www.nuget.org/packages/heirowDebug.ProjectZ) | 2026.10.20.1 | heirowDebug.ProjectZ | Native Project-Z live object inspection, editing, typed timelines and bounded s… |
| 2026-10-21 00:48:08 | [heirowDebug.WPF](https://www.nuget.org/packages/heirowDebug.WPF) | 2026.10.20.1 | heirowDebug.WPF | Live visual debugging for WPF applications with heirowDebug. |
| 2026-10-21 00:49:18 | [APIVerve.API.Magic8Ball](https://www.nuget.org/packages/APIVerve.API.Magic8Ball) | 1.2.2 | APIVerve | Magic 8-Ball is a fun tool that provides random predictions and answers like th… |
| 2026-10-21 00:49:21 | [APIVerve.API.JobPostings](https://www.nuget.org/packages/APIVerve.API.JobPostings) | 1.2.2 | APIVerve | Job Postings is a jobs API that returns the open positions on a company's publi… |
| 2026-10-21 00:49:25 | [APIVerve.API.TickerNews](https://www.nuget.org/packages/APIVerve.API.TickerNews) | 1.2.2 | APIVerve | Ticker News is a stock news API that returns the latest news stories about one… |
| 2026-10-21 00:49:35 | [APIVerve.API.IBondRates](https://www.nuget.org/packages/APIVerve.API.IBondRates) | 1.2.2 | APIVerve | I-Bond Rates provides current and historical interest rates for US Series I Sav… |
| 2026-10-21 00:49:45 | [APIVerve.API.JobSearch](https://www.nuget.org/packages/APIVerve.API.JobSearch) | 1.2.2 | APIVerve | Job Search is a jobs API that searches the open positions at thousands of compa… |
| 2026-10-21 00:49:48 | [APIVerve.API.BalanceSheet](https://www.nuget.org/packages/APIVerve.API.BalanceSheet) | 1.2.2 | APIVerve | Balance Sheet is a stock balance sheet API that returns the statement of financ… |
| 2026-10-21 00:49:54 | [APIVerve.API.DTCLookup](https://www.nuget.org/packages/APIVerve.API.DTCLookup) | 1.2.2 | APIVerve | DTC Lookup explains OBD-II diagnostic trouble codes such as P0301 or U0100. It… |
| 2026-10-21 00:50:03 | [APIVerve.API.TickerSymbols](https://www.nuget.org/packages/APIVerve.API.TickerSymbols) | 1.2.2 | APIVerve | Ticker Symbols identifies what a ticker symbol is and where it trades. Look up… |
| 2026-10-21 00:54:52 | [Vestigium.Helpers.FileSystemPaths](https://www.nuget.org/packages/Vestigium.Helpers.FileSystemPaths) | 1.4.0 | Vestigium | Path meaning: resolve, sanitize, tokenize, and long-path handling. |
| 2026-10-21 01:03:35 | [Haukcode.SigNet](https://www.nuget.org/packages/Haukcode.SigNet) | 0.1.4 | Hakan Lindestaf | A Sig-Net (secure CoAP-based DMX512 over IP) library for .NET: Sender role and… |
| 2026-10-21 01:09:29 | [Paicore.DocumentAPI](https://www.nuget.org/packages/Paicore.DocumentAPI) | 1.0.1 | Paicore | Document API for ASP.NET Core |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
