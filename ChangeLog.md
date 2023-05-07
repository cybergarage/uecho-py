# Change Log

## 1.1.0 - 2023/xx/xx
- Update Controller::post_message() to reduce the wait time

## 1.0.3 - 2023/05/07
- Updated the standard manufacturer code database based on the latest MCA (Manufacturer Code List) from the ECHONET Consortium
- Updated the standard object database based on the latest MRA (Machine Readable Appendix) version 1.2.0 from the ECHONET Consortium

## 1.0.2 - 2023/01/05
- Fix Device to set correct description property maps
- Update StandardDatabase to store property types and capacities more collectly
- Updated the standard manufacturer code database based on the latest MCA (Manufacturer Code List) from the ECHONET Consortium
- Add uechobench for benchmarking

## 1.0.1 - 2022/07/18
- Update manufacture database based on latest MCL of ECHONET Consortium
- Updated the standard object database based on the latest MRA (Machine Readable Appendix) version 1.1.1 from the ECHONET Consortium

## 1.0.0 - 2022/04/17
- Add Device class to create original devices of ECHONET Lite

## 0.8.5 - 2021/12/18
- Add a manufacture database based on MCA (Manufacturer Code List) of ECHONET Consortium
- Updated the standard object database based on the latest MRA (Machine Readable Appendix) version 1.0.0 from the ECHONET Consortium
- Update uechosearch to print all mandatory read properties using the standard database in the verbose mode
- Update ControleListener to listen object and property updates
- Add Property::post_message() and send_message()

## 0.8.4 - 2021/12/05
- Add ControleListener to listen to response and announce messages for nodes
- Change to ignore self multicast and unicast messages
- Improve uechosearch to print all mandatory readable property values using the standard database in the verbose mode

## 0.8.3 - 2021/11/23
- Add standard manufacture and object database of ECHONET Lite
- Add Controller::get_standard_manufacturer() and get_standard_object()
- Update Manager::start() to be able to set bind interface addresses

## 0.8.2 - 2021/11/14
- The first public release
- Fix Controller::stop() not to hung up on Linux platforms
