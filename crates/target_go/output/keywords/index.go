package jtd_codegen_e2e
type For = string
type Object = string
type Root struct {
	For For `json:"for"`
	Object Object `json:"object"`
}
