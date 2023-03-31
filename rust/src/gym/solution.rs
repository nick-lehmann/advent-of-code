use super::transform::FromInput;

pub type Error = String;

pub trait Solution<Args, Output>
// where
//     Output: std::str::FromStr + std::fmt::Debug + Clone + PartialEq,
{
    type Output: ToString;

    fn solve(&self, raw: &str) -> Self::Output;
}

/// Implementation of the `Solution` trait for 1-ary infallible functions.
impl<Func, Arg, Output> Solution<Arg, Output> for Func
where
    Func: Fn(Arg) -> Result<Output, Error>,
    Arg: FromInput,
    Output: ToString + std::fmt::Debug + Clone + PartialEq,
{
    type Output = Output;

    fn solve(&self, raw: &str) -> Output {
        let arg = Arg::from_input(raw).unwrap();
        (self)(arg).unwrap()
    }
}
