import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ActivatedRoute } from '@angular/router';
import { Company } from '../../models/company';
import { Vacancy } from '../../models/vacancy';
import { CompanyService } from '../../services/company.service';

@Component({
  selector: 'app-onecompany',
  imports: [CommonModule, RouterModule],
  templateUrl: './onecompany.component.html',
  styleUrl: './onecompany.component.css'
})
export class OnecompanyComponent implements OnInit {
  company: Company | undefined;
  vacancies: Vacancy[] = [];

  constructor(
    private route: ActivatedRoute,
    private companyService: CompanyService
  ) { }

  ngOnInit(): void {
    this.getCompany();
  }

  getCompany(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.companyService.getCompany(id)
      .subscribe(company => this.company = company);
    this.companyService.getCompanyVacancies(id)
      .subscribe(vacancies => this.vacancies = vacancies);
  }
}
