import sys
import os

# Ensure the root directory is in the path
sys.path.append(os.getcwd())

from sophia.cortex.glyphwave import GlyphwaveCodec
from sophia.main import SophiaMind

def test_glyphwave_cascadian():
    print("[TEST] Testing GlyphwaveCodec cascadian locality...")
    codec = GlyphwaveCodec()
    text = "The fog rolls over the ancient cedars. No worries, eh?"
    modulated = codec.generate_holographic_fragment(text, locality="cascadian")
    print(f"Modulated output:\n{modulated}")
    
    # Check for cascadian anchors
    anchors = ["🌲", "🏔️", "🍁", "🌧️", "🌊"]
    found_anchor = any(anchor in modulated for anchor in anchors)
    assert found_anchor, "No Cascadian anchors found in modulated output"
    print("[SUCCESS] Cascadian anchors detected.")
    
    # Check for noise
    noise_chars = ["~", "·", "°", "◌", "▿"]
    found_noise = any(noise in modulated for noise in noise_chars)
    assert found_noise, "No Cascadian noise detected in modulated output"
    print("[SUCCESS] Cascadian noise detected.")

def test_sophia_system_prompt():
    print("[TEST] Testing SophiaMind system prompt update...")
    mind = SophiaMind()
    prompt = mind.system_prompt
    print(f"System Prompt Snippet: {prompt[:200]}...")
    
    assert "CASCADIAN" in prompt
    assert "Canadian" in prompt
    assert "PNW" in prompt
    assert "eh" in prompt
    assert "zed" in prompt
    print("[SUCCESS] System prompt correctly updated with PNW/Canadian markers.")

if __name__ == "__main__":
    try:
        test_glyphwave_cascadian()
        print("-" * 20)
        test_sophia_system_prompt()
        print("\n[ALL TESTS PASSED]")
    except Exception as e:
        print(f"\n[TEST FAILED] {e}")
        sys.exit(1)
