function calculate(string) {
  try {
    const result = Function('"use strict"; return (' + string + ')')();
    return result;
  } catch (error) {
    return 'Invalid expression';
  }
}
