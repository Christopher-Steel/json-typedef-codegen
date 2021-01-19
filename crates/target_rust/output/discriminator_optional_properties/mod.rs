
use serde::{Deserialize, Serialize};





#[derive(Serialize, Deserialize)]
#[serde(tag = "foo")]
pub enum Root {

	#[serde(rename = "bar")]
	Bar(RootBar),

}




#[derive(Serialize, Deserialize)]
pub struct RootBar {





    #[serde(rename = "baz")]
    #[serde(skip_serializing_if = "Option::is_none")]
    pub baz: Option<Box<Vec<String>>>,





    #[serde(rename = "quux")]
    #[serde(skip_serializing_if = "Option::is_none")]
    pub quux: Option<Box<bool>>,

}
