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

class FloatArray {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.nums = null;
    }
    else {
      if (initObj.hasOwnProperty('nums')) {
        this.nums = initObj.nums
      }
      else {
        this.nums = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FloatArray
    // Serialize message field [nums]
    bufferOffset = _arraySerializer.float32(obj.nums, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FloatArray
    let len;
    let data = new FloatArray(null);
    // Deserialize message field [nums]
    data.nums = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.nums.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cs476/FloatArray';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8a327f765b70d8bd267a8d96beb763ec';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] nums
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FloatArray(null);
    if (msg.nums !== undefined) {
      resolved.nums = msg.nums;
    }
    else {
      resolved.nums = []
    }

    return resolved;
    }
};

module.exports = FloatArray;
