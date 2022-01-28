const DEFAULT_MESSAGE = 'Expected {lval}. Got {rval}';

/**
 * Asserts whether two values equal each other
 *
 * @param  {any}     rval             Right-side value
 * @param  {any}     lval             Left-side value
 * @param  {?string} fallbackMessage  The message to display if the values don't match
 * @throws {Error}
 */
module.exports = (rval, lval, fallbackMessage = DEFAULT_MESSAGE) => {
  if (rval !== lval) {
    const message = fallbackMessage
      .replace('{rval}', rval)
      .replace('{lval}', lval);

    throw new Error(message);
  }
};
