# Change Log

## 0.9.0 - 2022/??/??

- Add Device class to create original ECHONET Lite devices easily

## 0.8.5 - 2021/12/??

- Update standard object database based on Machine Readable Appendix Release M of ECHONET consortium
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