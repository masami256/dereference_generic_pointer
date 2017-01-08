import gdb


color_green = '\033[92m'
color_reset = '\033[0m'

class DereferenceGenricPointer(gdb.Command):
    """
    Dereference an address.
    This command helps to do dereference an address.

    When you want to to dereference an address $rbp - 8, you need to do following command 
    x/s *(char **) ($rbp - 0x8)

    It's ok, but bit complex. so this dgp command helps do so.

    syntax:
    dgp [Format] [Address expression]
    e.g.
    dgp s $rbp - 8
    dgp x/gx $rbp - 8

    Format and Address expression are same as gdb's.
    """

    def __init__(self):
        super(DereferenceGenricPointer, self).__init__('dgp', gdb.COMMAND_SUPPORT, gdb.COMPLETE_NONE, True)

    def invoke(self, arg, from_tty):
        args = arg.split(' ')
        if len(args) < 2:
            return 

        self.reg_size = self.register_size(args[1])

        dereference_cmd = self.create_dereference_cmd(args)
        if dereference_cmd == None:
            return

        cmd = 'x/%sx %s' % (self.reg_size, dereference_cmd)
        if cmd == None:
            print(ret)
            return 
    
        ret = self.execute(cmd)
        pointer_addr = self.get_address_value(ret)

        ret = self.dereference(args[0], pointer_addr)

        print(ret)

    def dereference(self, base_cmd, addr):
        cmd = 'x/%s %s' % (base_cmd, addr)
        ret = self.execute(cmd)
        return ret

    def get_pointer_address(self, register):
        cmd = 'x/%sx %s' % (self.reg_size, register)
        return self.execute(cmd)

    def execute(self, cmd):
        print('%s[*]execute: %s%s' % (color_green, cmd, color_reset))
        return gdb.execute(cmd, to_string = True)

    def create_dereference_cmd(self, args):
        symbol = '+'
        offset = 0

        args_len = len(args)

        if args_len == 3:
            if self.is_symbol(args[2]):
                symbol = args[2][0]
                offset = args[2][1:]
                if offset == '':
                    offset = 0
        elif args_len == 4:
            symbol = args[2]
            offset = args[3]

        return '%s %s %s' % (args[1], symbol, offset)

    def is_symbol(self, arg):
        return arg[0] == '+' or arg[0] == '-'

    def get_address_value(self, result):
        tmp = result.split(':')
        return tmp[1].strip()

    def register_size(self, reg):
        if reg[1] == 'r':
            return 'g'
        elif reg[1] == 'e':
            return 'w'
        
        return ''

DereferenceGenricPointer()
