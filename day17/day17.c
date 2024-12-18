#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <math.h>

#define MAXLEN 32


struct vm_t {
  unsigned long a, b, c, ip, op;
  char output[MAXLEN];
};


static void vm_reset(struct vm_t *vm, unsigned long a) {
  vm->a = a;
  vm->b = vm->c = vm->ip = vm->op = 0;
}


static unsigned long vm_combo(struct vm_t *vm, unsigned long operand) {
  if (operand >= 0 && operand <= 3)
    return operand;

  switch (operand) {
    case 4: return vm->a;
    case 5: return vm->b;
    case 6: return vm->c;
  }

  assert(0);
  return 0;
}


static int vm_tick(struct vm_t *vm, char *program) {
  char opcode = program[vm->ip++];

  if (opcode < 0)
    return 1;

  char operand = program[vm->ip++];

  switch(opcode) {
    case 0:
      vm->a /= pow(2, vm_combo(vm, operand));
      break;
    case 1:
      vm->b ^= operand;
      break;
    case 2:
      vm->b = vm_combo(vm, operand) % 8;
      break;
    case 3:
      if (vm->a)
        vm->ip = operand;
      break;
    case 4:
      vm->b ^= vm->c;
      break;
    case 5:
      vm->output[vm->op++] = vm_combo(vm, operand) % 8;
      break;
    case 6:
      vm->b = vm ->a / pow(2, vm_combo(vm, operand));
      break;
    case 7:
      vm->c = vm ->a / pow(2, vm_combo(vm, operand));
      break;
    default: assert(0);
  }

  return 0;
}


static void vm_execute(struct vm_t *vm, unsigned long a, char *program) {
  vm_reset(vm, a);
  while (!vm_tick(vm, program));
}


static long search_a(long start, char *program, size_t progidx) {
  struct vm_t vm;

  for (long a = start * 8; a < start * 8 + 8; ++a) {
    vm_execute(&vm, a, program);

    if (vm.op > 0 && vm.output[0] == program[progidx]) {
      if (progidx == 0)
        return a;

      long r = search_a(a, program, progidx - 1);
      if (r >= 0)
        return r;
    }
  }

  return -1;
}


static unsigned long find_quine(char *program, size_t proglen) {
  return search_a(0, program, proglen - 1);
}


static void print_array(char *arr, size_t n) {
  for (size_t i=0; i < n; ++i) {
    putchar(arr[i] + '0');
    putchar(i < n - 1 ? ',' : '\n');
  }
}


static size_t read_input(long *a, char *program) {
  int i;
  char progline[MAXLEN];

  scanf("Register A: %lu\n", a);
  scanf("Register B: 0\n");
  scanf("Register C: 0\n");
  scanf("\n");
  scanf("Program: %31s", progline);

  for (i=0; i < strlen(progline); i+=2)
    program[i/2] = progline[i] - '0';
  program[i/2] = -1;

  return i/2;
}


int main(int argc, char* argv[]) {
  long a;
  char program[MAXLEN];
  size_t proglen = read_input(&a, program);
  struct vm_t vm;

  printf("a=%lu ", a);
  print_array(program, proglen);

  vm_execute(&vm, a, program);
  print_array(vm.output, vm.op);

  a = find_quine(program, proglen);
  printf("Found quine: %lu\n", a);

  return 0;
}
