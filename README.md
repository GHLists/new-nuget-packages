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

## Latest list — 2026-11-08 20:21 UTC

New packages created between 2026-11-08 19:18 UTC and 2026-11-08 20:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-08T20-21-03-051519Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-08 19:18:57 | [TarsSdk](https://www.nuget.org/packages/TarsSdk) | 0.2.0 | Legendari | Client SDK for TARS — the self-hosted managed-agents platform (agents, durable… |
| 2026-11-08 19:28:32 | [Tessaro.Optional](https://www.nuget.org/packages/Tessaro.Optional) | 0.0.1 | Igor Tessaro | Java's Optional, the .NET way: model absence explicitly with a fluent, zero-dep… |
| 2026-11-08 19:32:57 | [ATK.Command.Explorer](https://www.nuget.org/packages/ATK.Command.Explorer) | 0.1.0 | Alexander Tkacuk | Stellt die Metadaten aller Commands einer WebApi als HTTP-Endpunkt bereit. Das… |
| 2026-11-08 19:42:59 | [Binbuy.Payments](https://www.nuget.org/packages/Binbuy.Payments) | 0.1.0 | bgunnarsson | Payment methods, the gateway contract, attempts, the transaction ledger and the… |
| 2026-11-08 19:43:00 | [Binbuy.Client](https://www.nuget.org/packages/Binbuy.Client) | 0.1.0 | bgunnarsson | A typed HTTP client implementing the Binbuy.Contracts admin interfaces against… |
| 2026-11-08 19:43:00 | [Binbuy.Payments.Straumur](https://www.nuget.org/packages/Binbuy.Payments.Straumur) | 0.1.0 | bgunnarsson | The Straumur hosted checkout payment gateway. |
| 2026-11-08 19:43:01 | [Binbuy.Persistence.SqlServer](https://www.nuget.org/packages/Binbuy.Persistence.SqlServer) | 0.1.0 | bgunnarsson | SQL Server migrations and connection settings for the Binbuy database. |
| 2026-11-08 19:43:02 | [Binbuy.Shipping.Easyship](https://www.nuget.org/packages/Binbuy.Shipping.Easyship) | 0.1.0 | bgunnarsson | Easyship shipping aggregator over its public API: rates, booking with labels, l… |
| 2026-11-08 19:43:02 | [Binbuy.Integrations](https://www.nuget.org/packages/Binbuy.Integrations) | 0.1.0 | bgunnarsson | Search indexing, marketing and analytics dispatch, outgoing webhooks and receip… |
| 2026-11-08 19:43:03 | [Binbuy.Shipping.DhlExpress](https://www.nuget.org/packages/Binbuy.Shipping.DhlExpress) | 0.1.0 | bgunnarsson | DHL Express shipping carrier over the MyDHL API: live rates, booking with label… |
| 2026-11-08 19:43:03 | [Binbuy.Persistence.PostgreSql](https://www.nuget.org/packages/Binbuy.Persistence.PostgreSql) | 0.1.0 | bgunnarsson | PostgreSQL migrations and connection settings for the Binbuy database. |
| 2026-11-08 19:43:04 | [Exceptionable](https://www.nuget.org/packages/Exceptionable) | 0.1.0 | Exceptionable | Public attributes for declaring exception contracts. |
| 2026-11-08 19:43:04 | [Binbuy.Kernel](https://www.nuget.org/packages/Binbuy.Kernel) | 0.1.0 | bgunnarsson | Money, currency, rounding, tax maths, ids, context and results shared by every… |
| 2026-11-08 19:43:04 | [Exceptionable.Analyzers](https://www.nuget.org/packages/Exceptionable.Analyzers) | 0.1.0 | Exceptionable | Roslyn analyzer for Exceptionable exception contracts. |
| 2026-11-08 19:43:04 | [Binbuy.Shipping.Flytjandi](https://www.nuget.org/packages/Binbuy.Shipping.Flytjandi) | 0.1.0 | bgunnarsson | Flytjandi (Eimskip domestic freight) as a manually fulfilled carrier with confi… |
| 2026-11-08 19:43:05 | [Binbuy.Cart](https://www.nuget.org/packages/Binbuy.Cart) | 0.1.0 | bgunnarsson | Carts: token identity, merge on login, linked lines, custom data, re-pricing wi… |
| 2026-11-08 19:43:05 | [Binbuy.Pricing](https://www.nuget.org/packages/Binbuy.Pricing) | 0.1.0 | bgunnarsson | Tax classes and rates, price lists, the price resolution pipeline and order tot… |
| 2026-11-08 19:43:06 | [Binbuy.Hosting](https://www.nuget.org/packages/Binbuy.Hosting) | 0.1.0 | bgunnarsson | AddBinbuy() and MapBinbuy(): registers every module and maps the Binbuy APIs, f… |
| 2026-11-08 19:43:06 | [Binbuy.Accounting.Dk](https://www.nuget.org/packages/Binbuy.Accounting.Dk) | 0.1.0 | bgunnarsson | DK (dkPlus) accounting connector: invoices and credit notes with unique referen… |
| 2026-11-08 19:43:07 | [Binbuy.Checkout](https://www.nuget.org/packages/Binbuy.Checkout) | 0.1.0 | bgunnarsson | Checkout sessions: validation pipeline, frozen order snapshot, stock and discou… |
| 2026-11-08 19:43:08 | [Binbuy.Shipping.Posturinn](https://www.nuget.org/packages/Binbuy.Shipping.Posturinn) | 0.1.0 | bgunnarsson | Pósturinn (Icelandic Post) shipping carrier: services, prices, pickup points, b… |
| 2026-11-08 19:43:08 | [Binbuy.Accounting.BusinessCentral](https://www.nuget.org/packages/Binbuy.Accounting.BusinessCentral) | 0.1.0 | bgunnarsson | Microsoft Dynamics 365 Business Central accounting connector over API v2.0: sal… |
| 2026-11-08 19:43:09 | [Binbuy.Marketing.Mailchimp](https://www.nuget.org/packages/Binbuy.Marketing.Mailchimp) | 0.1.0 | bgunnarsson | Mailchimp e-commerce: paid orders with their products and customer, refunds, ca… |
| 2026-11-08 19:43:09 | [Binbuy.Shipping.DhlLocationFinder](https://www.nuget.org/packages/Binbuy.Shipping.DhlLocationFinder) | 0.1.0 | bgunnarsson | DHL service points from the DHL Location Finder API, offered as a pickup shippi… |
| 2026-11-08 19:43:10 | [Binbuy.Catalog](https://www.nuget.org/packages/Binbuy.Catalog) | 0.1.0 | bgunnarsson | Categories, products, variant groups and variants, translations, per-store over… |
| 2026-11-08 19:43:10 | [Binbuy.Shipping.Bring](https://www.nuget.org/packages/Binbuy.Shipping.Bring) | 0.1.0 | bgunnarsson | Bring shipping carrier over the Mybring APIs: Shipping Guide rates, pickup poin… |
| 2026-11-08 19:43:11 | [Binbuy.Payments.Netgiro](https://www.nuget.org/packages/Binbuy.Payments.Netgiro) | 0.1.0 | bgunnarsson | Netgíró invoice and instalment payments through the Netgíró hosted payment page… |
| 2026-11-08 19:43:11 | [Binbuy.Marketing.Meta](https://www.nuget.org/packages/Binbuy.Marketing.Meta) | 0.1.0 | bgunnarsson | Meta Conversions API: purchases and cart events sent server-side with hashed cu… |
| 2026-11-08 19:43:12 | [Binbuy.Customers](https://www.nuget.org/packages/Binbuy.Customers) | 0.1.0 | bgunnarsson | Customers, addresses, groups, consent, shopper sign-in and GDPR export and eras… |
| 2026-11-08 19:43:13 | [Binbuy.Platform](https://www.nuget.org/packages/Binbuy.Platform) | 0.1.0 | bgunnarsson | Outbox, job leases, audit log, idempotency, admin identity, RBAC and API conven… |
| 2026-11-08 19:43:13 | [Binbuy.Stores](https://www.nuget.org/packages/Binbuy.Stores) | 0.1.0 | bgunnarsson | Stores, locales, currencies, countries, zones and per-request store resolution. |
| 2026-11-08 19:43:14 | [Binbuy.Notifications](https://www.nuget.org/packages/Binbuy.Notifications) | 0.1.0 | bgunnarsson | Customer and staff emails from outbox events: Scriban templates per store and l… |
| 2026-11-08 19:43:14 | [Binbuy.Search.Algolia](https://www.nuget.org/packages/Binbuy.Search.Algolia) | 0.1.0 | bgunnarsson | Algolia search: products and categories indexed per store, locale and currency… |
| 2026-11-08 19:43:15 | [Binbuy.Payments.Adyen](https://www.nuget.org/packages/Binbuy.Payments.Adyen) | 0.1.0 | bgunnarsson | The Adyen Checkout hosted payment gateway. |
| 2026-11-08 19:43:15 | [Binbuy.Umbraco.U17](https://www.nuget.org/packages/Binbuy.Umbraco.U17) | 0.1.0 | bgunnarsson | Binbuy for Umbraco 17: embedded or remote Binbuy, catalog sync, routing, Delive… |
| 2026-11-08 19:43:16 | [Binbuy.B2B](https://www.nuget.org/packages/Binbuy.B2B) | 0.1.0 | bgunnarsson | B2B: companies with members and roles, quotes with negotiated prices that check… |
| 2026-11-08 19:43:16 | [Binbuy.Shipping](https://www.nuget.org/packages/Binbuy.Shipping) | 0.1.0 | bgunnarsson | Shipping methods, rating, the carrier contract, shipments and tracking. |
| 2026-11-08 19:43:17 | [Binbuy.Promotions](https://www.nuget.org/packages/Binbuy.Promotions) | 0.1.0 | bgunnarsson | Discounts, coupons, code generation, atomic redemption, the quantity allocator… |
| 2026-11-08 19:43:18 | [Binbuy.Inventory](https://www.nuget.org/packages/Binbuy.Inventory) | 0.1.0 | bgunnarsson | Stock locations, stock items, movements, reservations with expiry, buffers and… |
| 2026-11-08 19:43:18 | [Binbuy.Payments.Teya](https://www.nuget.org/packages/Binbuy.Payments.Teya) | 0.1.0 | bgunnarsson | Teya (ex-Borgun) SecurePay hosted payment page with the RPG API, and Teya Hoste… |
| 2026-11-08 19:43:19 | [Binbuy.Persistence](https://www.nuget.org/packages/Binbuy.Persistence) | 0.1.0 | bgunnarsson | The one DbContext, naming conventions, SQL dialects and conditional-update help… |
| 2026-11-08 19:43:19 | [Binbuy.Marketing.Klaviyo](https://www.nuget.org/packages/Binbuy.Marketing.Klaviyo) | 0.1.0 | bgunnarsson | Klaviyo: order and cart events for flows, and email list subscription when the… |
| 2026-11-08 19:43:20 | [Binbuy.Shipping.Dropp](https://www.nuget.org/packages/Binbuy.Shipping.Dropp) | 0.1.0 | bgunnarsson | Dropp parcel lockers and home delivery in Iceland, as a shipping carrier. |
| 2026-11-08 19:43:20 | [Binbuy.Contracts](https://www.nuget.org/packages/Binbuy.Contracts) | 0.1.0 | bgunnarsson | The admin service interfaces and their request and response types, used by CMS… |
| 2026-11-08 19:43:21 | [Binbuy.Marketing.Ga4](https://www.nuget.org/packages/Binbuy.Marketing.Ga4) | 0.1.0 | bgunnarsson | Google Analytics 4 over the Measurement Protocol: purchases, refunds and cart e… |
| 2026-11-08 19:43:21 | [Binbuy.Umbraco.U18](https://www.nuget.org/packages/Binbuy.Umbraco.U18) | 0.1.0 | bgunnarsson | Binbuy for Umbraco 18: embedded or remote Binbuy, catalog sync, routing, Delive… |
| 2026-11-08 19:43:22 | [Binbuy.Payments.Stripe](https://www.nuget.org/packages/Binbuy.Payments.Stripe) | 0.1.0 | bgunnarsson | The Stripe Checkout payment gateway. |
| 2026-11-08 19:43:22 | [Binbuy.Persistence.Sqlite](https://www.nuget.org/packages/Binbuy.Persistence.Sqlite) | 0.1.0 | bgunnarsson | SQLite migrations and connection settings for the Binbuy database. |
| 2026-11-08 19:43:23 | [Binbuy.Shipping.PostNord](https://www.nuget.org/packages/Binbuy.Shipping.PostNord) | 0.1.0 | bgunnarsson | PostNord shipping carrier: service points, EDI booking with PDF labels, and tra… |
| 2026-11-08 19:43:24 | [Binbuy.Payments.SiminnPay](https://www.nuget.org/packages/Binbuy.Payments.SiminnPay) | 0.1.0 | bgunnarsson | The Síminn Pay push-to-phone payment gateway. |
| 2026-11-08 19:43:24 | [Binbuy.Accounting](https://www.nuget.org/packages/Binbuy.Accounting) | 0.1.0 | bgunnarsson | Accounting and ERP exports: a frozen, ERP-neutral sales document per order and… |
| 2026-11-08 19:43:25 | [Binbuy.Payments.TeyaLoans](https://www.nuget.org/packages/Binbuy.Payments.TeyaLoans) | 0.1.0 | bgunnarsson | The Teya consumer loans (Borgun Consumer Loans API v3) payment gateway. |
| 2026-11-08 19:43:25 | [Binbuy.Orders](https://www.nuget.org/packages/Binbuy.Orders) | 0.1.0 | bgunnarsson | Orders with order, payment and fulfilment state machines, per-store order numbe… |
| 2026-11-08 19:43:26 | [Binbuy.Payments.Klarna](https://www.nuget.org/packages/Binbuy.Payments.Klarna) | 0.1.0 | bgunnarsson | The Klarna Hosted Payment Page gateway. |
| 2026-11-08 19:43:27 | [Binbuy.Accounting.Payday](https://www.nuget.org/packages/Binbuy.Accounting.Payday) | 0.1.0 | bgunnarsson | Payday accounting connector: invoices booked or drafted with their payments, cu… |
| 2026-11-08 19:43:27 | [Binbuy.Subscriptions](https://www.nuget.org/packages/Binbuy.Subscriptions) | 0.1.0 | bgunnarsson | Subscriptions: recurring orders on a schedule, renewed by a leased job that cha… |
| 2026-11-08 19:43:28 | [Binbuy.Payments.VippsMobilePay](https://www.nuget.org/packages/Binbuy.Payments.VippsMobilePay) | 0.1.0 | bgunnarsson | The Vipps MobilePay ePayment gateway. |
| 2026-11-08 19:43:28 | [Binbuy.Shipping.Samskip](https://www.nuget.org/packages/Binbuy.Shipping.Samskip) | 0.1.0 | bgunnarsson | Samskip domestic freight as a manually fulfilled carrier with configured servic… |
| 2026-11-08 19:47:34 | [Averenium.Serilog.Sinks.RabbitMQ.Amqp](https://www.nuget.org/packages/Averenium.Serilog.Sinks.RabbitMQ.Amqp) | 0.1.0-preview-01 | Averenium | Serilog sink that writes log events to RabbitMQ 4.x over AMQP 1.0 using the off… |
| 2026-11-08 19:52:34 | [Novolis.Cad.Drawing](https://www.nuget.org/packages/Novolis.Cad.Drawing) | 2026.1.0.47 | Novolis | Avalonia-free technical drawing: orthographic projection, mesh sectioning, meas… |
| 2026-11-08 19:52:37 | [Novolis.Cad.Generation](https://www.nuget.org/packages/Novolis.Cad.Generation) | 2026.1.0.47 | Novolis | Avalonia-free CAD model generator contract. Generators return documents and hie… |
| 2026-11-08 19:52:38 | [Novolis.Cad.Hierarchy](https://www.nuget.org/packages/Novolis.Cad.Hierarchy) | 2026.1.0.47 | Novolis | Avalonia-free semantic CAD hierarchy: assemblies, parts, references, ownership,… |
| 2026-11-08 19:52:41 | [Novolis.Cad.Visibility](https://www.nuget.org/packages/Novolis.Cad.Visibility) | 2026.1.0.47 | Novolis | Hierarchical Inherit/Visible/Hidden object visibility for CAD documents. Sessio… |
| 2026-11-08 20:08:10 | [MyPackag](https://www.nuget.org/packages/MyPackag) | 1.0.0 | NaziIlka | A .NET library for simplifying microservice communication configuration using g… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
