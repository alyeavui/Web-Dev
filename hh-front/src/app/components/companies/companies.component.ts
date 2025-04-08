import { Component } from '@angular/core';
import { Company } from '../../models/company.model';
import { CompanyService } from '../../services/company.service';
import { Vacancy } from '../../models/vacancy.model';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-companies',
  imports: [CommonModule],
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent {
  companies: Company[] = [];
  selectedCompanyVacancies: Vacancy[] = [];

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((data) => {
      this.companies = data;
    });
  }

  onCompanyClick(companyId: number) {
    this.companyService.getCompanyVacancies(companyId).subscribe((data) => {
      this.selectedCompanyVacancies = data;
    });
  }
}
