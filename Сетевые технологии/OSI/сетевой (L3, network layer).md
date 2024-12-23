сетевой (L3, network layer)
========================

Этот уровень отвечает за маршрутизацию данных внутри сети между компьютерами. Здесь уже появляются такие термины, как «маршрутизаторы» и «IP-адреса».

Маршрутизаторы позволяют разным сетям общаться друг с другом: они используют MAC-адреса, чтобы построить путь от одного устройства к другому.

Данные на сетевом уровне представляются в виде пакетов. Такие пакеты похожи на фреймы из канального уровня, но используют другие адреса получателя и отправителя — IP-адреса.

Чтобы получить IP-адрес обоих устройств (отправителя и получателя), существует протокол ARP (address resolution protocol). Он умеет конвертировать MAC- в IP-адрес и наоборот.

Фрейм

| IP-адрес отправителя | IP-адрес получателя | Данные |