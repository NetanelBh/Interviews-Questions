const matchPar = (arr) => {
  const stack = [];

  for (let i=0; i<arr.length; i++) {
    const currentValue = arr[i];
    // If the value is opening parenthesis, insert to stack
    if (currentValue === '(' || currentValue === '[' || currentValue === '{') {
      stack.push(currentValue);
    }
    else {
      // Check if the closing parenthesis match the last open parenthesis
      const stackVal = stack.pop();
      switch (currentValue) {
        case ')':
          if (stackVal !== '(') {
            return false;
          }
          break;
        case ']':
          if (stackVal !== '[') {
            return false;
          }
          break;
        case '}':
          if (stackVal !== '{') {
            return false;
          }
          break;
        default:
          break;
      }
    }
  }

  // If the stack is empty, either all are matches or the given array is empty
  if (stack.length === 0) {
    return true;
  }
  return false;
};