// Auto-generated. Do not edit!

// (in-package cs476.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Chain2D {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.config = null;
      this.W = null;
      this.L = null;
      this.D = null;
    }
    else {
      if (initObj.hasOwnProperty('config')) {
        this.config = initObj.config
      }
      else {
        this.config = [];
      }
      if (initObj.hasOwnProperty('W')) {
        this.W = initObj.W
      }
      else {
        this.W = 0.0;
      }
      if (initObj.hasOwnProperty('L')) {
        this.L = initObj.L
      }
      else {
        this.L = 0.0;
      }
      if (initObj.hasOwnProperty('D')) {
        this.D = initObj.D
      }
      else {
        this.D = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Chain2D
    // Serialize message field [config]
    bufferOffset = _arraySerializer.float32(obj.config, buffer, bufferOffset, null);
    // Serialize message field [W]
    bufferOffset = _serializer.float32(obj.W, buffer, bufferOffset);
    // Serialize message field [L]
    bufferOffset = _serializer.float32(obj.L, buffer, bufferOffset);
    // Serialize message field [D]
    bufferOffset = _serializer.float32(obj.D, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Chain2D
    let len;
    let data = new Chain2D(null);
    // Deserialize message field [config]
    data.config = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [W]
    data.W = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [L]
    data.L = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [D]
    data.D = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.config.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cs476/Chain2D';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd7a949109af612580b026ed4500df1c3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] config
    float32 W
    float32 L
    float32 D  
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Chain2D(null);
    if (msg.config !== undefined) {
      resolved.config = msg.config;
    }
    else {
      resolved.config = []
    }

    if (msg.W !== undefined) {
      resolved.W = msg.W;
    }
    else {
      resolved.W = 0.0
    }

    if (msg.L !== undefined) {
      resolved.L = msg.L;
    }
    else {
      resolved.L = 0.0
    }

    if (msg.D !== undefined) {
      resolved.D = msg.D;
    }
    else {
      resolved.D = 0.0
    }

    return resolved;
    }
};

module.exports = Chain2D;
