SELECT		appln_id, appln_auth, appln_filing_year
FROM		sw_201_appln
WHERE		appln_filing_year >= 2006
	OR	appln_auth = 'JP'	-- JP: Japan