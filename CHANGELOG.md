# Change Log

## 1.0.2 - 2022/xx/xx0

- Fix to set correct description property maps

## 1.0.1 - 2022/07/18

- Update manufacture database based on latest MCL of ECHONET Consortium
- Update standard device database based on MRA v1.1.1 of ECHONET Consortium

## 1.0.0 - 2022/04/17

- Add Device class to create original devices of ECHONET Lite

## 0.8.5 - 2021/12/18

- Add a manufacture database based on MCA (Manufacturer Code List) of ECHONET Consortium
- Update standard object database based on MRA (Machine Readable Appendix) v1.0.0 of ECHONET consortium
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
