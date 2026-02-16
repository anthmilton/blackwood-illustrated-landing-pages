# LANDING PAGE CLEANUP & UPGRADE PLAN
## Memory Bridge Books Focus
**Created:** 2026-02-16  
**Purpose:** Rebrand landing page to Memory Bridge Books only, add all 12 books, organize by category

---

## CURRENT ISSUES

1. **Branding:** Still says "Blackwood Illustrated" (old brand)
2. **Missing books:** Only shows 6 books, missing 6 occupational books
3. **No Etsy links:** Only Amazon links present
4. **No organization:** Books not grouped by theme
5. **Mixed genres:** Gothic/kawaii links still in navigation (need to remove)

---

## NEW STRUCTURE

### **Rebrand to Memory Bridge Books**
- Logo/header: "Memory Bridge Books by Margaret Whitmore"
- Tagline: "Therapeutic Coloring for Memory Care"
- Remove all Blackwood Illustrated references
- Remove links to gothic/kawaii/bass pages

### **Hero Section**
- Headline: "Therapeutic Coloring Books That Honor Dignity"
- Subhead: "Designed specifically for seniors with dementia and Alzheimer's. Large print, era-accurate themes, dignified content."
- Featured images: Mix of covers from all 3 categories
- CTA buttons: "Shop on Amazon" + "Shop on Etsy" (dual buttons)

### **Book Categories (3 Sections)**

**Section 1: Classic Memory Care (3 books)**
- Remember When: 1950s Memory Care
- Sunday Drive: Classic Cars
- Main Street Memories

**Section 2: Working Life Collection (6 books)**
*(Occupational series - your differentiator)*
- Built With Hands: Boomer Edition
- Built With Hands: Vintage 1950s Trades  
- The Open Road & Field: Boomer Edition
- The Open Road & Field: Outdoorsman's
- Service & Uniform: Boomer Edition
- Service & Uniform: Vintage 1950s

**Section 3: Bold & Easy Collection (3 books)**
*(Fishing/outdoor themes for seniors)*
- Bold & Easy Bass Fishing
- Bold & Easy Trout Fishing
- Bold & Easy Saltwater Fishing

---

## UPDATED BOOKS.JSON

Need to add the 12th book and update structure:

```json
{
  "memory-care-classic": [
    {
      "title": "Remember When: 1950s Memory Care",
      "asin": "B0GLN61M3J",
      "etsyUrl": "",
      "status": "live",
      "cover": "remember-when.jpg"
    },
    {
      "title": "Sunday Drive: Classic Cars",
      "asin": "B0GLNTXF43",
      "etsyUrl": "https://www.etsy.com/ca/listing/4458215603/sunday-drive-classic-cars-memory-care",
      "status": "live",
      "cover": "sunday-drive.jpg"
    },
    {
      "title": "Main Street Memories",
      "asin": "B0GLN8L5GB",
      "etsyUrl": "",
      "status": "live",
      "cover": "main-street-memories.jpg"
    }
  ],
  "working-life-collection": [
    {
      "title": "Built With Hands: Boomer Edition",
      "asin": "B0GN98P31F",
      "etsyUrl": "https://www.etsy.com/ca/listing/4457776635/built-with-hands-boomer-edition-memory",
      "status": "live",
      "cover": "built-with-hands-boomer.png"
    },
    {
      "title": "Built With Hands: Vintage 1950s Trades",
      "asin": "B0GMXB29GZ",
      "etsyUrl": "",
      "status": "live",
      "cover": null
    },
    {
      "title": "The Open Road & Field: Boomer Edition",
      "asin": "B0GN9XPXFK",
      "etsyUrl": "https://www.etsy.com/ca/listing/4458204309/the-open-road-field-boomer-edition",
      "status": "live",
      "cover": "open-road-boomer.png"
    },
    {
      "title": "The Open Road & Field: Outdoorsman's",
      "asin": "B0GMX5D4Y1",
      "etsyUrl": "",
      "status": "live",
      "cover": null
    },
    {
      "title": "Service & Uniform: Boomer Edition",
      "asin": "B0GN9F3W73",
      "etsyUrl": "https://www.etsy.com/ca/listing/4458214992/service-uniform-boomer-edition-memory",
      "status": "live",
      "cover": "service-uniform-boomer.png"
    },
    {
      "title": "Service & Uniform: Vintage 1950s",
      "asin": "B0GN38NLPY",
      "etsyUrl": "",
      "status": "live",
      "cover": null
    }
  ],
  "bold-easy-collection": [
    {
      "title": "Bold & Easy Bass Fishing",
      "asin": "B0GL1RR48J",
      "etsyUrl": "",
      "status": "live",
      "cover": "big bold bass cover.png"
    },
    {
      "title": "Bold & Easy Trout Fishing",
      "asin": "B0GHQPZLYZ",
      "etsyUrl": "",
      "status": "live",
      "cover": "bold-easy-trout.jpg"
    },
    {
      "title": "Bold & Easy Saltwater Fishing",
      "asin": "B0GLNDM6MC",
      "etsyUrl": "",
      "status": "live",
      "cover": "bold-easy-saltwater.jpg"
    }
  ]
}
```

---

## CARD LAYOUT FOR EACH BOOK

```html
<div class="book-card">
    <img src="[cover-image]" alt="[book title]">
    <h3>[Book Title]</h3>
    <p>[Short description]</p>
    <div class="button-group">
        <a href="https://www.amazon.com/dp/[ASIN]" class="btn btn-amazon">
            Amazon
        </a>
        <a href="[Etsy URL]" class="btn btn-etsy">
            Etsy
        </a>
    </div>
</div>
```

**Button styling:**
- Amazon button: Dark/neutral color
- Etsy button: Orange/accent color (#F16521 - Etsy brand color)
- Side-by-side layout
- If no Etsy link yet, hide Etsy button or show "Coming Soon"

---

## SECTION HEADERS

**Classic Memory Care**
- Headline: "1950s Nostalgia & Americana"
- Subtext: "Classic cars, small-town memories, and simpler times. Perfect for seniors born in the 1930s-1950s."

**Working Life Collection**
- Headline: "Activities for Men with Dementia"  
- Subtext: "Honoring tradesmen, factory workers, farmers, truckers, and first responders. Reconnect to occupational identity."
- Badge: "NEW" or "Our Differentiator"

**Bold & Easy Collection**
- Headline: "Fishing & Outdoor Memories"
- Subtext: "For seniors who loved the water and the outdoors. Large-format designs perfect for trembling hands."

---

## FOOTER UPDATES

**Add links:**
- Amazon Author Central: https://www.amazon.com/author/memorybridgebooks
- Etsy Shop: https://www.etsy.com/shop/MemoryBridgeBooks (once you set shop name)

**Add social proof (once available):**
- "As featured on..."
- Customer testimonials
- "Trusted by [X] caregivers and memory care facilities"

---

## FILES TO UPDATE

1. **index.html** → Rebrand to Memory Bridge Books, clean nav
2. **memorycare.html** → Rename to just show all 12 books
3. **books.json** → Add 12th book, add Etsy URLs, reorganize structure
4. **Remove/hide:**
   - bass-fishing.html (content absorbed into main page)
   - gothic.html (hide from nav, keep file for legacy links)
   - kawaii.html (hide from nav, keep file for legacy links)
   - hub.html (replace with new index.html)

---

## IMPLEMENTATION STEPS

### **Step 1: Update books.json**
- Add Service & Uniform Vintage 1950s (ASIN: B0GN38NLPY)
- Add Etsy URLs for 4 live listings
- Reorganize into 3 categories (classic, working-life, bold-easy)
- Add cover filenames for occupational books (once you have them)

### **Step 2: Create new index.html**
- Memory Bridge Books branding
- Hero section with 3-category showcase
- All 12 books displayed
- Amazon + Etsy dual buttons per book
- Clean footer with Author Central + Etsy shop links

### **Step 3: Update navigation**
- Remove links to gothic/kawaii/bass pages
- Simple nav: Home | About | Shop (Amazon) | Shop (Etsy)

### **Step 4: Test all links**
- Verify all 12 Amazon links work
- Verify 4 Etsy links work
- Test on mobile + desktop

### **Step 5: Deploy**
- Push to Vercel
- Test live site
- Update any marketing materials with new URL

---

## OPTIONAL ENHANCEMENTS

**About Section:**
- Add Margaret Whitmore bio (use the short form)
- "Why Memory Bridge Books is different"
- Dignity-first design philosophy

**Testimonials Section:**
- Once you have reviews, feature them prominently
- Quote cards with caregiver stories

**Email Signup:**
- "Get notified when new books launch"
- Build email list for future promotions

**Badge System:**
- "NEW" badges on recent books
- "Bestseller" badges once you have sales data
- "On Etsy" badges for digital availability

---

## COLOR PALETTE UPDATE

**Current (Blackwood):**
- Primary: #2D2D2D (charcoal)
- Background: #F5F1E8 (vellum)
- Accent: #D4AF37 (gold)

**Suggested (Memory Bridge):**
- Keep the warm, nostalgic palette
- Add Etsy orange for Etsy buttons: #F16521
- Add soft blue for trust/care: #6B9AC4
- Keep current colors but rebrand as "Memory Bridge" aesthetic

---

## TIMELINE

**Step 1 (Today):** Update books.json with 12th book + Etsy URLs
**Step 2 (Today):** Create new index.html with all 12 books
**Step 3 (Today):** Test locally
**Step 4 (Today/Tomorrow):** Deploy to Vercel
**Step 5 (As covers ready):** Add cover images for occupational books

---

## QUESTIONS FOR YOU

1. **Do you have cover images** for the 6 occupational books (vintage + boomer editions)? If yes, send them and I'll add to books.json.

2. **Etsy shop URL:** Once all 12 are listed, what's your main Etsy shop URL? (For footer link)

3. **Domain:** Do you want to register memorybridgebooks.com and point it to this landing page?

4. **About page:** Want me to create a separate About page with Margaret Whitmore bio + story?

5. **Keep old pages:** Should I keep bass-fishing.html, gothic.html, kawaii.html as hidden legacy pages (for old links) or delete them entirely?

---

## NEXT ACTIONS

**Tell me:**
1. ✅ If this structure looks good
2. ✅ Whether you have cover images for occupational books
3. ✅ Your Etsy shop main URL (once all listings are up)

**Then I'll:**
1. Update books.json
2. Create new index.html with all 12 books + Etsy links
3. Test everything
4. Give you deployment instructions

---

**Status:** Cleanup plan ready. Waiting on your green light + cover images + Etsy shop URL. 🛠️
