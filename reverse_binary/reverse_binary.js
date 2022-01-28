const assert = require('./utils/assert');

const BIN_STR_REGEX = /\b(0|1[0,1]*)\b/;

/**
 * Reverses a binary number.
 *
 * @param   {string} binaryNumber Input binary number (e.g. '10011')
 * @returns {string} Reversed binary number (e.g. '11001')
 */
const reverseBinary = (binaryNumber) => {
  assert(BIN_STR_REGEX.test(binaryNumber), true, `Invalid binary number: ${binaryNumber}`);

  if (binaryNumber.length === 1) {
    return binaryNumber;
  }

  // An alternative solution would have been that of using the bitwise shift operators
  // For instance, see https://www.geeksforgeeks.org/reverse-actual-bits-given-number/
  // Although this solution may seem less efficient, IMO it is the most readable
  return binaryNumber.split('').reverse().join('');
};

assert(reverseBinary('0'), '0');
assert(reverseBinary('1'), '1');
assert(reverseBinary('11'), '11');
assert(reverseBinary('1101'), '1011');

module.exports = reverseBinary;
