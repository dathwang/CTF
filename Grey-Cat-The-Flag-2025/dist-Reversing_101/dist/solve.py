import angr
import logging 

logging.getLogger("angr").setLevel(logging.INFO)

def hook(l=None):
    if l:
        locals().update(l)
    import IPython
    IPython.embed(banner1='', exit_msg='', confirm_exit=False)
    exit(0)

def main():
    proj = angr.Project("chal")

    init_state = proj.factory.entry_state()
    simulation = proj.factory.simgr(init_state)

    simulation.explore(find=0x402FBE, veritesting=True)

    if simulation.found:
        solution_state = simulation.found[0]
        print(solution_state.posix.stdin.concretize())

    hook(locals())

if __name__=="__main__":
    main()