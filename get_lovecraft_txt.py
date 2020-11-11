import os
from pathlib import Path

from pyquery import PyQuery as pq
from tqdm.notebook import tqdm

pages = [
    "https://www.hplovecraft.com/writings/texts/fiction/a.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/as.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mm.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/az.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/bec.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/bc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/bws.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/b.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/cc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/cdw.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/cu.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/c.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/cb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/clc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/cs.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ca.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/crc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/cy.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/d.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/de.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/dat.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/di.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ds.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/dq.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/dwh.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/dh.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ee.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ec.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/eo.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/faj.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/f.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/fb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ge.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/gm.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hd.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/he.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hwr.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hn.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hwb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hmb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hrh.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hm.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/h.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/hy.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ibid.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/iv.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/iwe.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/lt.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/lgb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ld.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/lf.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ms.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/m.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mo.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mez.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mys.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/mg.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/nc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/no.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/n.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ob.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/og.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/oa.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/o.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/pm.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ph.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/pg.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/p.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/qi.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/rw.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/rdsj.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/sc.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/sot.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/soi.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/soidd.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/sh.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/sk.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/sm.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/src.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/shh.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/s.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/se.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/te.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tom.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tm.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/td.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tgsk.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tas.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/t.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tjr.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/trap.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tr.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/th.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/tbb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/up.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/u.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/vof.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/wmb.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/wid.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/ws.aspx",
    "https://www.hplovecraft.com/writings/texts/fiction/wd.aspx"
]
dirname = os.path.dirname(__file__)
FILE_NAME = os.path.join(dirname, 'data/raw_text.txt')
print('FILE_NAME: ', FILE_NAME)
def get_and_save_remote_text():
    if os.path.exists(FILE_NAME):
        print('File already exists! Skipping download...')
        return
    else:
        print(f"The file {FILE_NAME} does not exist")

    page_contents = []
    for page in tqdm(pages):
        d = pq(url=page)
        text_nodes = []
        d('tr').each(lambda i, el: text_nodes.append(el.text_content()))
        longest_string = max(text_nodes, key=len)
        page_contents.append(longest_string)

    with open(FILE_NAME, 'w') as file:
        file.write("\n".join(page_contents))


if __name__ == "__main__":
    get_and_save_remote_text()
