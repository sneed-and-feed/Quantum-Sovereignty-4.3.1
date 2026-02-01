import os
import google.generativeai as genai
from .aletheia_protocols import PRIME_DIRECTIVE, STACK

class AletheiaLens:
    """
    [ALETHEIA] The Optic Nerve.
    Module for autopsy of text to prevent Ontological Force from infecting cognition.
    """
    def __init__(self, api_key=None, model_name="gemini-1.5-pro"):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        if self.api_key:
            genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def _call_gemini(self, prompt, context_text):
        """
        Internal wrapper for Gemini calls.
        """
        if not self.api_key:
            return f"[MOCK] Analysis of: {context_text[:30]}..."
            
        full_prompt = f"{PRIME_DIRECTIVE}\n\nTASK: {prompt}\n\nINPUT TEXT:\n{context_text}"
        try:
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            return f"[ERROR] Gemini call failed: {str(e)}"

    def perceive(self, raw_text):
        """
        Runs the Ingestion -> Linguistics -> Mechanics stack.
        Returns a 'Sanitized Perception' of the text.
        """
        print(f"  [~] [ALETHEIA] Autopsying text: {len(raw_text)} chars...")
        
        # 1. Structural Decomposition
        structure = self._call_gemini(STACK['structure'], raw_text)
        
        # 2. Anomaly Scan (The 'Virus Check')
        anomalies = self._call_gemini(STACK['linguistics'], raw_text)
        
        # 3. Mechanics Exposure
        mechanics = self._call_gemini(STACK['mechanics'], raw_text)
        
        # Synthesis
        draft_analysis = f"STRUCTURE:\n{structure}\n\nANOMALIES:\n{anomalies}\n\nMECHANICS:\n{mechanics}"
        
        return draft_analysis

    def enforce_epistemic_hygiene(self, agent_output):
        """
        Runs Prompt #4 (Self-Audit) on the AGENT'S OWN OUTPUT.
        Ensures Sophia never becomes coercive.
        """
        print(f"  [~] [ALETHEIA] Auditing self-manifestation...")
        audit = self._call_gemini(STACK['self_audit'], agent_output)
        
        if "VIOLATION FOUND" in audit.upper() or "ONTOLOGICAL FORCE" in audit.upper():
            print("  [!] [ALETHEIA] Epistemic violation detected in output. Recalibrating...")
            # If the audit found issues, we ask the model to rewrite based on the audit
            correction = self._call_gemini(f"Rewrite this text to be strictly neutral based on this audit:\n{audit}", agent_output)
            return correction
        
        return agent_output

    def map_risk_surface(self, raw_text):
        """
        Identifies high-risk vectors (manipulation, identity hooks).
        """
        # Placeholder for Prompt #5 logic
        risk_analysis = self._call_gemini("Identify high-risk narrative vectors. Output 'RISK_LEVEL: HIGH/LOW' and then vectors.", raw_text)
        risk_level = "HIGH" if "RISK_LEVEL: HIGH" in risk_analysis.upper() else "LOW"
        
        return {
            "risk_level": risk_level,
            "vectors": risk_analysis
        }
