"""
AI-Powered Visual Data Analytics and Business Intelligence Platform - Streamlit dashboard (MILESTONE 4)
--------------------------------------------------
Run:  streamlit run app.py

Pages:
  🏠 Home          overview + status
  👷 PPE Detection image / video          (Milestone 1)
  📄 Documents     upload + search manuals (Milestone 2)
  🤖 Ask AI        LangGraph agent          (Milestone 3)
  📊 Dashboard     KPIs + charts            (Milestone 4)
  📋 Report        PDF download             (Milestone 4)

Remember: Streamlit re-runs this whole file on every click.
  - @st.cache_resource  -> load heavy things only once
  - st.session_state    -> remember results between clicks
  - save data only inside a button, or it is saved again on every rerun
"""

import os
import tempfile

import cv2
import streamlit as st

import knowledge_base as kb
import storage
import vision
from agent import ask_agent
from documents import process_file
from llm import MODEL, has_key
from report import build_pdf, write_summary

st.set_page_config(
    page_title="AI-Powered Visual Data Analytics and Business Intelligence Platform",
    page_icon="🦺",
    layout="wide",
)

# On Streamlit Cloud the API key comes from "Secrets"
try:
    if "GEMINI_API_KEY" in st.secrets:
        os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass


# ── load once ──────────────────────────────────────────────
@st.cache_resource
def get_model():
    return vision.load_model()


@st.cache_resource
def load_sample_manual():
    """If the knowledge base is empty (e.g. fresh cloud start), add a manual automatically."""
    if kb.total_chunks() == 0:
        for name in ["safety_manual.pdf", "sample_safety_manual.txt"]:
            path = os.path.join(vision.BASE_DIR, "data", name)
            if os.path.exists(path):
                kb.add_document(process_file(path), name)
                return name
    return None


def save_upload(uploaded):
    suffix = os.path.splitext(uploaded.name)[1]  # keep the real extension
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded.getbuffer())
        return tmp.name


model = get_model()
load_sample_manual()

# ── sidebar ────────────────────────────────────────────────

with st.sidebar:

    # ─────────────────────────────────────────
    # BRAND
    # ─────────────────────────────────────────

    st.title("🦺 VisionDesk AI")
    st.caption("Multimodal Workplace Safety")

    st.divider()

    # ─────────────────────────────────────────
    # NAVIGATION
    # ─────────────────────────────────────────

    st.markdown("### 🧭 Navigation")

    page = st.radio(
        "Go to",
        [
            "🏠 Home",
            "👷 PPE Detection",
            "📄 Documents",
            "🤖 Ask AI",
            "📊 Dashboard",
            "📋 Report"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    # ─────────────────────────────────────────
    # SYSTEM STATUS
    # ─────────────────────────────────────────

    st.markdown("### ⚙️ System Status")

    with st.container(border=True):

        if model:
            st.success("🟢 PPE Model Ready")
        else:
            st.error("🔴 PPE Model Missing")

        if has_key():
            st.success("🟢 Gemini Ready")
        else:
            st.warning("🟡 Gemini API Key Missing")

        st.info(f"📚 {kb.total_chunks()} knowledge chunks")

    st.divider()

    st.caption("VisionDesk AI")
    st.caption("Milestone 4 • Safety Intelligence")

# ══════════════════════════════════════════════════════════
# 🏠 HOME
# ══════════════════════════════════════════════════════════

if page == "🏠 Home":

    st.title("🦺 VisionDesk AI")
    st.caption("Multimodal Workplace Safety Intelligence")

    with st.container(border=True):

        st.subheader("Workplace Safety Intelligence")

        st.write(
            "Detect PPE violations, search safety documents, "
            "ask AI questions and generate compliance reports."
        )

    # ─────────────────────────────────────────────────────
    # KPI SECTION
    # ─────────────────────────────────────────────────────

    scans = storage.load_scans()
    k = storage.kpis(scans)

    st.subheader("📊 Safety Overview")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.metric(
                "👷 Inspections",
                k["scans"]
            )

    with c2:
        with st.container(border=True):
            st.metric(
                "🟢 Compliance",
                f"{k['compliance']}%"
                if k["compliance"] is not None else "0%"
            )

    with c3:
        with st.container(border=True):
            st.metric(
                "⚠️ Violations",
                k["violations"]
            )

    with c4:
        with st.container(border=True):
            st.metric(
                "📚 Knowledge",
                kb.total_chunks()
            )

    # ─────────────────────────────────────────────────────
    # QUICK ACTIONS
    # ─────────────────────────────────────────────────────

    st.divider()

    st.subheader("🚀 Quick Actions")

    a, b, c = st.columns(3)

    with a:
        with st.container(border=True):

            st.markdown("## 👷")
            st.subheader("PPE Detection")

            st.write(
                "Upload a workplace image or video "
                "and detect PPE violations."
            )

            st.button(
                "🔍 Analyze PPE",
                use_container_width=True
            )

    with b:
        with st.container(border=True):

            st.markdown("## 📄")
            st.subheader("Safety Documents")

            st.write(
                "Upload safety manuals and inspection "
                "documents to the knowledge base."
            )

            st.button(
                "📚 Open Documents",
                use_container_width=True
            )

    with c:
        with st.container(border=True):

            st.markdown("## 🤖")
            st.subheader("Ask Safety AI")

            st.write(
                "Ask questions using your safety documents "
                "and latest PPE detection."
            )

            st.button(
                "💬 Ask AI",
                use_container_width=True
            )


    # ─────────────────────────────────────────────────────
    # HOW IT WORKS
    # ─────────────────────────────────────────────────────

    st.divider()

    st.subheader("🔄 How VisionDesk AI Works")

    p1, p2, p3, p4 = st.columns(4)

    with p1:
        with st.container(border=True):
            st.markdown("## 1️⃣")
            st.subheader("Detect")
            st.caption("YOLO detects workers and PPE.")

    with p2:
        with st.container(border=True):
            st.markdown("## 2️⃣")
            st.subheader("Retrieve")
            st.caption("Relevant safety rules are retrieved.")

    with p3:
        with st.container(border=True):
            st.markdown("## 3️⃣")
            st.subheader("Ask AI")
            st.caption("Gemini answers using retrieved information.")

    with p4:
        with st.container(border=True):
            st.markdown("## 4️⃣")
            st.subheader("Report")
            st.caption("Inspection results become safety reports.")
    # ─────────────────────────────────────────────────────
    # SYSTEM STATUS
    # ─────────────────────────────────────────────────────

    st.divider()

    st.subheader("🔧 System Status")

    s1, s2, s3 = st.columns(3)

    with s1:
        with st.container(border=True):
            st.markdown("### 👷 PPE Model")

            if model:
                st.success("Ready")
            else:
                st.error("Model Not Found")

    with s2:
        with st.container(border=True):
            st.markdown("### 🤖 Gemini AI")

            if has_key():
                st.success("Connected")
            else:
                st.warning("API Key Required")

    with s3:
        with st.container(border=True):
            st.markdown("### 📚 Knowledge Base")

            st.metric(
                "Chunks",
                kb.total_chunks()
            )
# ══════════════════════════════════════════════════════════
# 👷 PPE DETECTION  (Milestone 1)
# ══════════════════════════════════════════════════════════
elif page == "👷 PPE Detection":
    st.header("👷 PPE Detection")
    if not model:
        st.error("best.pt not found in the project folder.")
        st.stop()

    with st.container(border=True):

        st.subheader("⚙️ Detection Settings")

        c1, c2 = st.columns(2)

        with c1:
            kind = st.radio(
                "Input",
                ["Image", "Video"],
                horizontal=True
            )

        with c2:
            conf = st.slider(
                "Confidence",
                0.1,
                0.9,
                0.4,
                0.05,
                help="Higher = fewer false alarms, but may miss some items"
            )

    if kind == "Image":
        file = st.file_uploader("Upload a site image", type=["jpg", "jpeg", "png"])
        if file and st.button("Analyze image", type="primary"):
            path = save_upload(file)
            dets = vision.detect(model, path, conf)
            result = vision.summarize(dets, file.name)
            storage.log_scan(file.name, result, "image")  # saved only on click
            st.session_state["last"] = {
                "name": file.name,
                "result": result,
                "dets": dets,
                "image": vision.draw(cv2.imread(path), dets),
            }
    else:
        file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
        every_n = st.slider("Check 1 of every N frames", 1, 30, 5)
        if file and st.button("Analyze video", type="primary"):
            with st.spinner("Analysing video..."):
                dets, preview, frames = vision.detect_video(
                    model, save_upload(file), every_n, conf
                )
            result = vision.summarize(dets, file.name)
            storage.log_scan(file.name, result, "video")
            st.session_state["last"] = {
                "name": f"{file.name} ({frames} frames)",
                "result": result,
                "dets": dets,
                "image": preview,
            }


    last = st.session_state.get("last")
    if last:
        st.divider()
        st.subheader("🔍 Detection Result")
        col1, col2 = st.columns([3, 2])
        with col1:
            if last["image"] is not None:
                st.image(
                    cv2.cvtColor(last["image"], cv2.COLOR_BGR2RGB),
                    caption=last["name"],
                    use_container_width=True
                )
        with col2:
                with st.container(border=True):

                    r = last["result"]

                    if r["compliant"]:
                        st.success("✅ COMPLIANT - no violations")
                    else:
                        st.error(
                            "🚨 VIOLATIONS: "
                            + ", ".join(sorted(set(r["violations"])))
                        )

                    st.subheader("📊 Detection Summary")

                    m1, m2, m3 = st.columns(3)

                    with m1:
                        st.metric(
                            "🔎 Objects Detected",
                            len(last["dets"])
                        )

                    with m2:
                        st.metric(
                            "⚠️ Violations",
                            len(r["violations"])
                        )

                    with m3:
                        st.metric(
                            "🦺 PPE Categories",
                            len(r["counts"])
                        )

                    st.divider()

                    st.subheader("🧾 Detection Details")

                    for item, count in r["counts"].items():
                        st.write(f"**{item}** — {count}")

                    if r["compliant"]:
                        st.success(
                            "🟢 COMPLIANT — No PPE violations detected."
                        )
                    else:
                        st.error("🔴 SAFETY VIOLATIONS DETECTED")

                        for violation in sorted(set(r["violations"])):
                            st.warning(f"⚠️ {violation}")

                    st.caption("💡 This result is available in Ask AI.")

# ══════════════════════════════════════════════════════════
# 📄 DOCUMENTS  (Milestone 2)
# ══════════════════════════════════════════════════════════
elif page == "📄 Documents":
    st.title("📄 Safety Document Center")

    st.info(
        "Upload safety manuals, inspection reports or incident reports. "
        "The documents become searchable by the AI."
    )

    st.subheader("📤 Upload Documents")
    files = st.file_uploader(
        "Upload manuals / inspection or incident reports",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True,
    )
    if files and st.button("Add to knowledge base", type="primary"):
        for f in files:
            chunks = process_file(save_upload(f))
            if chunks:
                kb.add_document(chunks, f.name)
                st.success(f"{f.name}: {len(chunks)} chunks added")
            else:
                st.warning(f"{f.name}: no text found (scanned PDF?)")
    st.divider()
    # st.subheader("📚 Knowledge Base")
    st.subheader("📚 Documents in the knowledge base")
    docs = kb.list_documents()
    if docs:
        st.table([{"document": name, "chunks": n} for name, n in docs.items()])
    else:
        st.info("No documents yet.")

    st.divider()
    st.subheader("🔍 Search Safety Documents")
    # st.subheader("🔍 Test search")
    q = st.text_input("Search", placeholder="When must goggles be worn?")
    if q:
        for r in kb.search(q):
            st.info(
                f"**{r['source']} #{r['chunk']}** (distance {r['distance']})\n\n{r['text']}"
            )


# ══════════════════════════════════════════════════════════
# 🤖 ASK AI  (Milestone 3 - LangGraph agent)
# ══════════════════════════════════════════════════════════
elif page == "🤖 Ask AI":
    st.title("🤖 Ask Safety AI")

    st.info(
        "Ask questions about PPE, workplace rules, safety procedures "
        "or your uploaded documents."
    )

    last = st.session_state.get("last")
    use_image = False
    if last:
        use_image = st.checkbox(
            f"Include last detection result ({last['name']})", value=True
        )
        if use_image:
            st.caption(last["result"]["text"])
            

    st.divider()

    st.subheader("💡 Example Questions")

    q1, q2, q3 = st.columns(3)

    with q1:
        with st.container(border=True):
            st.info("What PPE is required?")

    with q2:
        with st.container(border=True):
            st.info("What are the emergency procedures?")

    with q3:
        with st.container(border=True):
            st.info("Is this worker compliant?")
        
        #Question section
    st.divider()

    with st.container(border=True):

        st.subheader("💬 Ask your question")

        question = st.text_input(
            "Your question",
            placeholder="Is this worker compliant? Which rule applies?"
        )

        if st.button("🤖 Ask Safety AI", type="primary") and question:
            vis = last["result"] if (use_image and last) else None
            with st.spinner("Thinking..."):
                out = ask_agent(
                    question,
                    vision=vis["text"] if vis else "",
                    violations=vis["violations"] if vis else [],
                )
            st.session_state["answer"] = {"question": question, **out}
            st.session_state["voted"] = False
        
        #Answer section

    ans = st.session_state.get("answer")
    if ans:
        
        with st.container(border=True):

            st.subheader("🤖 AI Answer")

            st.write(ans["answer"])
        
        with st.expander("🔍 View AI reasoning / sources"):

            st.write(
                "**Steps:** " +
                " → ".join(ans["steps"])
            )

            st.markdown("### 📚 Sources")

            for d in ans["docs"]:
                st.caption(
                    f"[{d['source']} #{d['chunk']}] "
                    f"{d['text'][:200]}"
                )
            
        with st.expander("How the agent worked"):
            st.write("**Steps:** " + " → ".join(ans["steps"]))
            for d in ans["docs"]:
                st.caption(f"[{d['source']} #{d['chunk']}] {d['text'][:200]}")

        if not st.session_state.get("voted"):
            st.write("Was this answer helpful?")
            c1, c2 = st.columns(2)
            if c1.button("👍 Yes"):
                storage.log_feedback(ans["question"], True)
                st.session_state["voted"] = True
                st.rerun()
            if c2.button("👎 No"):
                storage.log_feedback(ans["question"], False)
                st.session_state["voted"] = True
                st.rerun()
        else:
            st.caption("Thanks for your feedback!")


# ══════════════════════════════════════════════════════════
# 📊 DASHBOARD  (Milestone 4)
# ══════════════════════════════════════════════════════════
elif page == "📊 Dashboard":
    st.title("📊 Safety Analytics")

    st.info(
        "Monitor workplace inspections, PPE compliance, "
        "violations and safety trends."
    )
    scans = storage.load_scans()
    k = storage.kpis(scans)

    st.subheader("📈 Key Performance Indicators")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        with st.container(border=True):
            st.metric("👷 Inspections", k["scans"])

    with c2:
        with st.container(border=True):
            st.metric(
                "🟢 Compliance Rate",
                f"{k['compliance']}%"
                if k["compliance"] is not None else "-"
            )

    with c3:
        with st.container(border=True):
            st.metric("⚠️ Total Violations", k["violations"])

    with c4:
        with st.container(border=True):
            st.metric(
                "⭐ Satisfaction",
                f"{k['satisfaction']}%"
                if k["satisfaction"] is not None else "-"
            )


    st.divider()
    st.subheader("📊 Safety Trends")

    if scans.empty:
        st.info("No data yet. Analyse some images in 👷 PPE Detection.")
    else:
        left, right = st.columns(2)

        with left:
            with st.container(border=True):

                st.subheader("⚠️ Violations by Type")

                counts = storage.violation_counts(scans)

                if len(counts):
                    st.bar_chart(counts)
                else:
                    st.success("No violations so far 🎉")

        with right:
            with st.container(border=True):

                st.subheader("📅 Violations per Day")

                daily = (
                    scans
                    .set_index("time")["violations"]
                    .resample("D")
                    .sum()
                )

                st.line_chart(daily)

    st.divider()

    with st.container(border=True):

        st.subheader("📋 Inspection History")

        st.dataframe(
            scans.sort_values("time", ascending=False),
            hide_index=True,
            use_container_width=True
        )
    if st.button("🗑️ Clear history"):
        storage.clear_all()
        st.rerun()


# ══════════════════════════════════════════════════════════
# 📋 REPORT  (Milestone 4)
# ══════════════════════════════════════════════════════════
elif page == "📋 Report":
    st.title("📋 Safety Compliance Report")

    st.info(
        "Generate a professional report from your workplace "
        "inspection data."
    )
    scans = storage.load_scans()
    
    if st.button("Generate report", type="primary"):
        k = storage.kpis(scans)
        counts = storage.violation_counts(scans)
        
        with st.spinner("Writing summary..."):
            summary = write_summary(k, counts)
        st.session_state["report"] = {
            "summary": summary,
            "pdf": build_pdf(k, counts, scans, summary),
        }

    rep = st.session_state.get("report")
    if rep:
        with st.container(border=True):

            st.subheader("📝 Report Summary")

            st.write(rep["summary"])
        st.download_button(
            "⬇️ Download PDF",
            rep["pdf"],
            file_name="safety_compliance_report.pdf",
            mime="application/pdf",
        )
        st.divider()

        st.subheader("📥 Download Report")

        d1, d2 = st.columns(2)

        with d1:
            with st.container(border=True):
                st.download_button(
                    "📄 Download PDF Report",
                    rep["pdf"],
                    file_name="safety_compliance_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

        with d2:
            with st.container(border=True):
                st.download_button(
                    "📊 Download CSV Data",
                    scans.to_csv(index=False),
                    file_name="scans.csv",
                    mime="text/csv",
                    use_container_width=True
                )
