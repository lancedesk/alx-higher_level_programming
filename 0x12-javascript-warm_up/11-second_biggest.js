#!/usr/bin/node
const nums = process.argv.slice(2);
if (process.argv.length <= 3) {
  console.log(0);
} else {
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
