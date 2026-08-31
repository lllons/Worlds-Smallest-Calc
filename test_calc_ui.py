# Tests for Calc_ui.py. Run with: python test_calc_ui.py
import io, sys, importlib.util, os

PASS = 0
FAIL = 0

def run(name, fn):
    global PASS, FAIL
    try:
        fn()
        PASS += 1
        print("ok - " + name)
    except AssertionError as e:
        FAIL += 1
        print("FAIL - " + name + ": " + str(e))
    except Exception as e:
        FAIL += 1
        print("ERROR - " + name + ": " + e.__class__.__name__ + ": " + str(e))

HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = importlib.util.spec_from_file_location("calc_ui", os.path.join(HERE, "Calc_ui.py"))
calc_ui = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(calc_ui)

def test_menu_expressions():
    for key, expr, desc in calc_ui.MENU:
        if expr == "quit":
            continue
        result = eval(expr, {}, {})
        assert result is not None, expr + " produced None"

def test_specific_2_plus_2():
    assert eval("2 + 2", {}, {}) == 4

def test_safety_empty_globals():
    try:
        eval("undefined_variable", {}, {})
        raise AssertionError("NameError was not raised")
    except NameError:
        pass

def test_show_prints_menu():
    buf = io.StringIO()
    saved = sys.stdout
    sys.stdout = buf
    try:
        calc_ui.show()
    finally:
        sys.stdout = saved
    out = buf.getvalue()
    for key, expr, desc in calc_ui.MENU:
        assert key in out
        assert expr in out

run("menu expressions evaluate", test_menu_expressions)
run("2 + 2 == 4", test_specific_2_plus_2)
run("eval with empty globals raises NameError", test_safety_empty_globals)
run("show() prints every menu entry", test_show_prints_menu)

print("")
print(str(PASS) + " passed, " + str(FAIL) + " failed")
sys.exit(0 if FAIL == 0 else 1)
