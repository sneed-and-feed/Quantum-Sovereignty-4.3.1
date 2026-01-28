use pyo3::prelude::*;

// Look for the gearbox module
mod gearbox;
use gearbox::HarmonicGearbox;

// CSH-1 Module
mod v2k_buffer;
use v2k_buffer::V2KBuffer;

/// The Iron Kernel Entry Point.
/// Note the change in signature: "m: &Bound<'_, PyModule>"
#[pymodule]
fn pleroma_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    // The "Bound" API uses add_class just like before, but the type is strictly checked.
    m.add_class::<HarmonicGearbox>()?;
    m.add_class::<V2KBuffer>()?;
    Ok(())
}