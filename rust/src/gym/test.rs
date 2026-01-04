// TODO: For a procedural macro, it would be cool if it would validate that the testcase exists on the fly.
macro_rules! aoc_test {
    ($func:ident, $year:expr, $day:expr, $testcase:expr) => {
        paste::paste! {
            #[test_log::test]
            fn [<test_ $year _ $day _ $func _example>]() {
                let _ = env_logger::builder().is_test(true).try_init();
                // let _ = env_logger::init();

                let testcases = get_testcases($testcase, $year, $day);
                let solution = $func.solve(&testcases[0].input);
                assert_eq!(solution.to_string(), testcases[0].solution);
            }

            #[test_log::test]
            fn [<test_ $year _ $day _ $func _puzzle>]() {
                let _ = env_logger::builder().is_test(true).try_init();
                // let _ = env_logger::init();

                let testcases = get_testcases($testcase, $year, $day);
                let solution = $func.solve(&testcases[1].input);
                assert_eq!(solution.to_string(), testcases[1].solution);
            }
        }
    };
}
pub(crate) use aoc_test;
