# SignalWild — Frontier Research Venture (Investor Site)

A static, responsive investor website for SignalWild. Includes a ten-slide deck (PDF), branded concept visual, and a clickable demonstration of a proposed individual-animal Communication Passport.

## Current stage

This is **research-stage investor communication**, not an operational animal translator. All passport scenarios and hardware are labelled as illustrative. No deployed proprietary hardware, translation accuracy, animal trials, customers, or revenues are claimed.

## Publish via GitHub Pages

1. Sign into GitHub and create a new **public** repository, suggested name `signalwild` (do not initialise it with an additional README if uploading via Git).
2. Upload **the contents of this directory** to the repository root (`index.html`, `README.md`, `SignalWild_Investor_Deck.pdf`, `.nojekyll`, `assets/`).
3. Open repository **Settings → Pages → Build and deployment → Deploy from a branch**. Choose `main` and `/(root)`; save.
4. GitHub will show the actual published site URL in Pages settings. For an account `priyankbakshi` and repo `signalwild`, the usual URL pattern would be `https://priyankbakshi.github.io/signalwild/`, but do not treat it as live until GitHub confirms deployment.
5. Test all nav links, the interactive passport tabs and the PDF link in the hosted site.

No external Javascript library, build step or server is required. All site links to assets are relative so they work under a GitHub Pages project path.

## Local preview

Open `index.html` in Chrome/Edge. For a local HTTP server, run `python3 -m http.server 8000` from this folder and visit http://localhost:8000.

## Editing

The website is a single `index.html` plus the hero visual. All textual content and styles are editable directly. The pitch deck PDF is mirrored in the site root; the editable PPTX is delivered separately.

## Evidence and claims

SignalWild aims to test whether a personalised model can help unfamiliar people interpret individual animal behaviour better than care notes, simple context models and species-wide AI. This is a hypothesis, not an achieved result. Real deployment will require appropriate consent, privacy and animal-welfare review.