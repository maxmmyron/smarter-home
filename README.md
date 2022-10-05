# smarter-home

CS3500 semester project: smart home control system

## Outline

The aim of this control system would be to simplify living. This smart home system would allow users to activate appliances, change the temperature, and maintain security over a home.

### Inputs

The primary input methods planned for this control system are the following:
- sensors attached to primary entry/exit points
- an automated plan that revolves around one family's day (waking up; leaving for work, school; shopping; arriving home from school, work; going to bed)
- voice input *or* remote smart appliance control from capable devices (smartphone, smart hub, etc.)
These inputs can be analyzed and interpreted within our software to determine the best course of action to take to achieve the desired result.

### Outputs

The primary outputs planned for this control system are the following:
- a change in temperature within rooms in the house
- a change in the security configuration of the house, for example:
  - doors locking/unlocking 
  - windows/blinds closing/opening
  - cameras activating/deactivating certain functionality (watch zones, package notifications, etc.)
- discrete actions being performed on electrical appliances within the house, for example: 
  - a TV turning on
  - lights turning on/off, dimming/brightening, changing color
  - oven preheating to a specific temperature
  
 Outputs can also include a data structure containing information about the state of the house, for example:
 - temperature of rooms
 - current power draw/power state of appliances
 - appliance battery levels
 - problematic events (break-ins, smoke-detection, carbon monoxide, etc.)

### Flowchart

The below flowchart shows a rough example of how such a system could function and be implemented:

![image](https://user-images.githubusercontent.com/41480159/193957205-6cc2e2cf-62c6-4ff5-a9c7-7325d022a554.png)
